Input Test
C   ______ _______  _____      _     _ __   _ _______ ______  
C  |  ____ |______ |     | ___ |     | | \  | |______ |     \ 
C  |_____| |______ |_____|     |_____| |  \_| |______ |_____/
C Version : 0.9.8.1     09/06/2023
C FreeCAD Version : 0.20.2 
C
C *************************************************************
C Original Step file : inputSTEP/DoubleCylinder/pieza1.stp
C
C Creation Date : 2023-06-11 18:17:30.153241
C Solid Cells   : 1
C Total Cells   : 4
C Surfaces      : 16
C Materials     : 0
C
C **************************************************************
1     0      1 -7 5 -3 -6 4 -2 8:-9 -6 7 5
           imp:n=1.0   imp:p=1.0   
C 
C ##########################################################
C              VOIDS 
C ##########################################################
C 
2     0      10 12 14 -15 -13 -11 ((-1:3:7:-8:-4:2) (9:-7):-5:6)
           imp:n=1.0   imp:p=1.0   
           $Automatic Generated Void Cell. Enclosure(-1.0, 2.0, -1.0, 2.0, -1.0, 2.0)
           $Enclosed cells : (1)
3     0      -16 (-10:11:-12:13:-14:15)
           imp:n=1.0   imp:p=1.0   
           $Graveyard_in
4     0      16
           imp:n=0     imp:p=0     
           $Graveyard
 
C ##########################################################
C                  SURFACE DEFINITION
C ##########################################################
1      PX   0.0000000e+00
2      PX   1.0000000e+00
3      PY   1.0000000e+00
4      PY   0.0000000e+00
5      PZ   0.0000000e+00
6      PZ   1.0000000e+00
7      P   -7.0710678e-01 -7.0710678e-01 -0.0000000e+00 -1.4142136e-01
8      C/Z      0.320000     0.320000     0.100000
9      C/Z      0.200000     0.200000     0.200000
10     PX  -1.0000000e+00
11     PX   2.0000000e+00
12     PY  -1.0000000e+00
13     PY   2.0000000e+00
14     PZ  -1.0000000e+00
15     PZ   2.0000000e+00
16     S   5.0000000e-01  5.0000000e-01  5.0000000e-01  2.6500377e+00
 
C 
MODE P
VOID 
NPS 1e6
PRDMP 2J -1
C SDEF PAR=P X=D1 Y=D2 Z=D3 
C SI1 -1.0000000e+00 2.0000000e+00 
C SI2 -1.0000000e+00 2.0000000e+00 
C SI3 -1.0000000e+00 2.0000000e+00 
C SP1 0  1 
C SP2 0  1 
C SP3 0  1 
SDEF PAR=P NRM=-1 SUR=16 WGT=2.2062463e+01 DIR=d1
SI1 0 1
SP1 -21 1
F4:P  1 
SD4   9.6000000e-01 