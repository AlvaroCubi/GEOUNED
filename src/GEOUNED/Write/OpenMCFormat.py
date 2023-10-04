##############################
# Module to write MCNP input #
##############################
from datetime import datetime

from GEOUNED.Utils.Functions import Surfaces_dict
from GEOUNED.Write.Functions import OpenMCSurface, changeSurfSign,  writeOpenMCregion,CardLine
from GEOUNED.Utils.Options.Classes import MCNP_numeric_format as nf
from GEOUNED.Utils.Options.Classes import Options as opt
from GEOUNED.CodeVersion import *
import FreeCAD
import copy
import math
import re

class OpenMC_input:
    def __init__(self,Meta,Surfaces,setting) :

       self.Cells    = Meta

       self.__getSurfaceTable__()
       self.__simplifyPlanes__(Surfaces)
       
       self.Surfaces = self.__sortedSurfaces__(Surfaces) 
       self.Materials = set()

    def writeXML(self,filename):
       print ('write OpenMC xml file {}'.format(filename))
       self.inpfile=open(filename,'w',encoding='utf-8')
       self.__write_xml_header__(filename)

       self.inpfile.write("<geometry>\n")
       self.__write_xml_cell_block__()
       self.inpfile.write(' \n')
       self.__write_xml_surface_block__()
       self.inpfile.write("</geometry>\n")
         
       self.inpfile.close()
       return                    

    def __write_xml_header__(self,fileout):
       Header = "<?xml version='1.0' encoding='UTF-8'?>\n"
       self.inpfile.write(Header)
       return
       
    def __write_xml_cell_block__(self):
       for i,cell in enumerate(self.Cells):
          if  cell.MatInfo == 'Graveyard' : continue
          self.__write_xml_cells__(cell)
       return

    def __write_xml_surface_block__(self):
       for surf in self.Surfaces[:-1]:
          self.__write_xml_surfaces__(surf)
       self.__write_xml_surfaces__(self.Surfaces[-1],boundary=True)

    def __write_xml_cells__(self,cell):
       """ Write the cell in xml OpenMC format """
       index = cell.__id__
       if index is None : return

       if cell.Material == 0: 
          matName = 'void'
       else:
          matName = '{}'.format(cell.Material) 

       OMCcell = '  <cell id="{}" material="{}" region="{}" universe="1"/>\n'.format( \
                                       index,\
                                       matName,\
                                       writeOpenMCregion(cell.Definition,'XML') ) 
       self.inpfile.write(OMCcell)
       return


    def __write_xml_surfaces__(self,surface,boundary=False):
       """ Write the surfaces in xml OpenMC format """

       surfType,coeffs = OpenMCSurface( surface.Type, surface.Surf)

       if not boundary:
          OMCsurf = '  <surface id="{}" type="{}" coeffs="{}" />\n'.format(surface.Index, surfType, coeffs)
       else:
          OMCsurf = '  <surface id="{}" type="{}" coeffs="{}" boundary="vacuum" />\n'.format(surface.Index, surfType, coeffs)

       self.inpfile.write(OMCsurf)
       return 
        
    def writePY(self,filename):
       print ('write OpenMC python script {}'.format(filename))

       # get all the materials present in the model
       for cell in self.Cells:
         if cell.Material != 0: 
           self.Materials.add(cell.Material)

       self.inpfile=open(filename,'w',encoding='utf-8')
       self.__write_py_header__(filename)

       if len(self.Materials) > 0 :
          self.inpfile.write("# Materials setup\n")
          self.__write_py_materials__()
       self.inpfile.write("\n")

       self.inpfile.write("# Surface setup\n")
       self.__write_py_surface_block__()
       self.inpfile.write("\n")

       self.inpfile.write('# Cell definition \n')
       self.__write_py_cell_block__()
         
       self.inpfile.close()
       return                    

    def __write_py_header__(self,fileout):
 
       Header = """\
# openMC geometry script generated by GEOUNED
import openmc

###############################################################################
# Define problem geometry
###############################################################################

"""
       self.inpfile.write(Header)
       return

    def __write_py_materials__(self):
        matList = tuple(sorted(self.Materials))
        strMat = []
        for m in matList:
           material = "M{} = openmc.Material(name='M{}')\n".format(m,m)
           self.inpfile.write(material)
           strMat.append('M{}'.format(m))

        collect = 'materials = openmc.Materials([{}])\n'.format(', '.join(strMat))
        self.inpfile.write(collect)
        self.inpfile.write('materials.export_to_xml()\n')


    def __write_py_surface_block__(self):

       for surf in self.Surfaces[:-1]:
          self.__write_py_surfaces__(surf)
       self.__write_py_surfaces__(self.Surfaces[-1],boundary=True)


    def __write_py_surfaces__(self,surface,boundary=False):
       """ Write the surfaces in xml OpenMC format """

       surfType,coeffs = OpenMCSurface(surface.Type, surface.Surf, outXML = False, quadricForm = opt.quadricPY)

       if not boundary:
          OMCsurf = 'S{} = openmc.{}({})\n'.format(surface.Index, surfType, coeffs)
       else:
          OMCsurf = 'S{} = openmc.{}({}, boundary_type="vacuum")\n'.format(surface.Index, surfType, coeffs)

       self.inpfile.write(OMCsurf)
       return 

    def __write_py_cell_block__(self):

       cellNames = []
       for i,cell in enumerate(self.Cells):
          if  cell.MatInfo == 'Graveyard' : continue
          self.__write_py_cells__(cell)
          if cell.__id__ is None : continue
          cellNames.append('C{}'.format(cell.__id__))

       geometry = "\ngeometry = openmc.Geometry([{}])\ngeometry.export_to_xml()\n".format(', '.join(cellNames)) 

       self.inpfile.write(geometry)
       return


    def __write_py_cells__(self,cell):
       """ Write the cell in xml OpenMC format """
       index = cell.__id__
       if index is None : return

       if cell.Material == 0: 
          OMCcell = 'C{} = openmc.Cell(region={})\n'.format(index, writeOpenMCregion(cell.Definition,'PY') ) 
       else:
          matName = 'M{}'.format(cell.Material) 
          OMCcell = 'C{} = openmc.Cell(fill={}, region={})\n'.format(index, matName, writeOpenMCregion(cell.Definition,'PY') ) 
       self.inpfile.write(OMCcell)
       return


    def __getSurfaceTable__(self):
       self.surfaceTable = {}
       self.__solidCells__ = 0
       self.__cells__      = 0
       self.__materials__ = set()
       
       for i, CellObj in enumerate(self.Cells):
          if CellObj.__id__ is None : continue
          self.__cells__ += 1
          if CellObj.Material != 0 :
             self.__materials__.add(CellObj.Material)

          surf = CellObj.Definition.getSurfacesNumbers()
          if not CellObj.Void : self.__solidCells__ += 1 
          for index in surf : 
              if index in self.surfaceTable.keys() :
                  self.surfaceTable[index].add(i)
              else:
                  self.surfaceTable[index] = {i}
       return

             
    def __simplifyPlanes__(self,Surfaces):
       offset = len(self.Cells)
       keys= self.surfaceTable.keys()

       for p in Surfaces['PX']:
          if p.Surf.Axis[0] < 0 :
            p.Surf.Axis = FreeCAD.Vector(1,0,0)
            self.__changeSurfSign__(p)
 
       for p in Surfaces['PY']:
          if p.Surf.Axis[1] < 0 :
            p.Surf.Axis = FreeCAD.Vector(0,1,0)
            self.__changeSurfSign__(p)
                                           
       for p in Surfaces['PZ']:
          if p.Surf.Axis[2] < 0 :
            p.Surf.Axis = FreeCAD.Vector(0,0,1)
            self.__changeSurfSign__(p)          
       return
    
    def __sortedSurfaces__(self,Surfaces):
        temp = Surfaces_dict(Surfaces)
        surfList = []
        for ind in range(Surfaces.IndexOffset, Surfaces.surfaceNumber + Surfaces.IndexOffset):
           s=temp.getSurface(ind+1)
           if s is not None :  
             surfList.append(s)
             temp.delSurface(ind+1)
        return surfList
    
    def __changeSurfSign__(self,p):

        if p.Index not in self.surfaceTable.keys() :
            print('{} Surface {} not used in cell definition)'.format(p.Type,p.Index),p.Surf.Axis,p.Surf.Position)
            return
        
        for ic in self.surfaceTable[p.Index] :
           surf = self.Cells[ic].Definition.getSurfacesNumbers()
           for s in surf :
             if s == p.Index : 
                changeSurfSign(s, self.Cells[ic].Definition)



    
