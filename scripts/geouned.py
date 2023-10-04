#!/usr/bin/python

# Path to GEOUNED Package
import sys

geo_path="C:\\Users\\Juan\\Documents\\work\\GEOUNED\\RepoGit\\GitHub\\GEOUNEDcode\\src"

sys.path.append(geo_path)
#sys.path.append([geo_path+"\\GEOUNED",geo_path+\GEOReverse\])
#sys.path.append("C:\\Users\\Juan\\Documents\\work\\GEOUNED\\RepoGit\\GitHub\\GEOUNEDcode\\src\\GEOUNED")

#sys.path.append(geo_path+'\\GEOReverse')

# linux distributions
# sys.path.append('/usr/lib64/freecad/lib64/')

import GEOUNED 
from  GEOReverse import reverse

runReverse = False
if len(sys.argv) < 2 :
   inifile = 'config.ini'

elif len(sys.argv) == 2 :
   if sys.argv[1] == '-r':
      runReverse = True
      inifile = 'configReverse.ini'
   else:
      inifile = sys.argv[1]

elif len(sys.argv) == 3:
   if   sys.argv[1] == '-r':
      runReverse = True
      inifile = sys.argv[2]
   elif sys.argv[2] == '-r':
      runReverse = True
      inifile = sys.argv[1]
   else:
      print('Bad option')
      exit()
else:
   print('Too many input arguments')
   exit()


if not runReverse :
  GEO = GEOUNED(inifile)
  GEO.SetOptions()
  GEO.Start()

else:
  print(inifile)
  reverse(inifile)
