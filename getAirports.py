import sys
sys.path.append('C:\\Users\\user\\qgis\\qgis_tools')

from qgis_tools import *


import urllib
import json

#url ="https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json"
#urllib.urlretrieve(url, "c:/temp/data.txt")

f = open('c:/temp/data.txt', 'r')
jdata = f.read()
f.close()
data = json.loads(jdata)

inx = 0
pts=[]
xs = []
ys = []
names = []
for j in data:
    xs += [float( j["lon"] )]
    ys += [float( j["lat"] )]
    names += [j["name"]]
    inx += 1
    if inx > 30:
        break

pts = [xs,ys]

curPtInx = 0
imgWidth = 10000
imgHight = 10000
outputWidth = 500
outputHeight = 500
dpi = 300
cx, cy = 0, 0

def doNext():
    global pts, curPtInx, imgWidth, imgHight, cx, cy
    
    if curPtInx < len(pts[0]):
        cx = pts[0][curPtInx]
        cy = pts[1][curPtInx]
        cx, cy = CoordinateTransform(4326, 3857, cx, cy)
        zoom2area( cx, cy, imgWidth, imgHight)
        curPtInx += 1

    
def onMapLoad():
    global pts, curPtInx, imgWidth, imgHight, cx, cy, dpi, names
   
    
    #captureImage2(   "c:/temp/" + str(cx) + "_" + str(cy),
    captureImage2(  "c:/temp/" + str(curPtInx-1) 
                        + "_"+ names[curPtInx-1],
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