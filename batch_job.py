import sys
sys.path.append('C:\\Users\\user\\qgis\\qgis_tools')

from qgis_tools import *

pts=[[13496849.583491117,13427468.542009214,12978182.73213968]
    ,[2882698.3315221076,2785696.282111045,4877589.175822471]]

curPtInx = 0
imgWidth = 10000
imgHight = 10000
outputWidth = 2500
outputHeight = 2500
dpi = 300
cx, cy = 0, 0

def doNext():
    global pts, curPtInx, imgWidth, imgHight, cx, cy
    
    if curPtInx < len(pts[0]):
        cx = pts[0][curPtInx]
        cy = pts[1][curPtInx]
        zoom2area( cx, cy, imgWidth, imgHight)
        curPtInx += 1

    
def onMapLoad():
    global pts, curPtInx, imgWidth, imgHight, cx, cy, dpi
   
#    captureImage(   "c:/temp/" + str(cx) + "_" + str(cy),
#                    "jpg",
#                    dpi,
#                    outputWidth,    # mm
#                    outputHeight)   # mm
    
    captureImage2(   "c:/temp/" + str(cx) + "_" + str(cy),
                    "jpg",
                    outputWidth,   # px
                    outputHeight)  # px
    
    if curPtInx >= len(pts[0]):
        iface.mapCanvas().mapCanvasRefreshed.disconnect(onMapLoad)
        print("All Done!! :)")
    else:
        doNext()

    
iface.mapCanvas().mapCanvasRefreshed.connect(onMapLoad)
doNext()