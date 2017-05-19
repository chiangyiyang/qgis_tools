from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.utils import iface


def zoom2area(canvas, x, y, width, height):
    canvas.setExtent(
            QgsRectangle(
                x - width/2, y - height/2, 
                x + width/2, y + height/2
                ))
    canvas.refresh()
    print("zoom to : ", x, y, x+width, y+height)



mapCanvas = iface.mapCanvas()
pts = [[13496849.583491117,13427468.542009214,12978182.73213968]
,[2882698.3315221076,2785696.282111045,4877589.175822471]]

x=pts[0][0]
y=pts[1][0]
width=5000
height=5000
zoom2area(
    mapCanvas, 
    x, y,
    width, height)
    