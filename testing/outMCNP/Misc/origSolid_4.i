Input Test
C   ______ _______  _____      _     _ __   _ _______ ______  
C  |  ____ |______ |     | ___ |     | | \  | |______ |     \ 
C  |_____| |______ |_____|     |_____| |  \_| |______ |_____/
C Version : 0.9.8.1     09/06/2023
C FreeCAD Version : 0.20.2 
C
C *************************************************************
C Original Step file : inputSTEP/Misc/origSolid_4.stp
C
C Creation Date : 2023-06-11 18:24:10.811023
C Solid Cells   : 1
C Total Cells   : 4
C Surfaces      : 13
C Materials     : 0
C
C **************************************************************
1     0      -1 2 3 -4 5 6
           imp:n=1.0   imp:p=1.0   
C 
C ##########################################################
C              VOIDS 
C ##########################################################
C 
2     0      7 9 11 -12 -10 -8 (1:-3:-5:-6:4:-2)
           imp:n=1.0   imp:p=1.0   
           $Automatic Generated Void Cell. Enclosure(632.592510012262, 642.6957218626895, -819.4575165637791, -809.6824181700947, 80.55000000000001, 91.42660769901653)
           $Enclosed cells : (1)
3     0      -13 (-7:8:-9:10:-11:12)
           imp:n=1.0   imp:p=1.0   
           $Graveyard_in
4     0      13
           imp:n=0     imp:p=0     
           $Graveyard
 
C ##########################################################
C                  SURFACE DEFINITION
C ##########################################################
1      P   -6.4278761e-01  7.6604444e-01  0.0000000e+00 -1.0310000e+03
2      P    7.6201758e-01  6.3940867e-01 -1.0240000e-01 -4.5562165e+01
3      P   -1.7566161e-01  9.8311828e-01 -5.1200023e-02 -9.1865328e+02
4      GQ   0.586824088833131  0.413175911166868  1.000000000000000
           0.984807753012326  0.000000000000000  0.000000000000000
          56.610684346873398 47.502004356187577 -172.000000000000000
          8741.500000019150320 
5      GQ   0.820511787921796  0.180190625432761  0.999297586645443
           0.767192593514886  0.047993543436043 -0.022456617478974
          -415.004308760156846 -197.655507714571911 -118.587708959932584
          56321.767683941616269 
6      P    9.0241813e-01  4.1935446e-01 -9.8910829e-02  2.2283276e+02
7      PX   6.3259251e+02
8      PX   6.4269572e+02
9      PY  -8.1945752e+02
10     PY  -8.0968242e+02
11     PZ   8.0550000e+01
12     PZ   9.1426608e+01
13     S   6.3764412e+02 -8.1456997e+02  8.5988304e+01  9.0649259e+00
 
C 
MODE P
VOID 
NPS 1e6
PRDMP 2J -1
C SDEF PAR=P X=D1 Y=D2 Z=D3 
C SI1 6.3259251e+02 6.4269572e+02 
C SI2 -8.1945752e+02 -8.0968242e+02 
C SI3 8.0550000e+01 9.1426608e+01 
C SP1 0  1 
C SP2 0  1 
C SP3 0  1 
SDEF PAR=P NRM=-1 SUR=13 WGT=2.5815372e+02 DIR=d1
SI1 0 1
SP1 -21 1
F4:P  1 
SD4   3.7916743e+01 