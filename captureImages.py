from qgis.utils import iface
from PyQt4.QtCore import *
from PyQt4.QtGui import *

rx = range(121,123)
ry = range(22,24)
cx = 121
cy = 22
dd = 1
isDone = False

mycvs = iface.mapCanvas()

def doSomething(name):
    ##Output using Map Composer#########
    # set up composition
    mapRenderer = iface.mapCanvas().mapRenderer()
    c = QgsComposition(mapRenderer)
    c.setPlotStyle(QgsComposition.Print)

    # add a map to the composition
    x, y =0,0
    w, h = c.paperWidth(), c.paperHeight()
    composerMap = QgsComposerMap(c, x, y, w, h)
    c.addItem(composerMap)

    ##Output to a raster image#########
    dpi = c.printResolution()
    dpmm = dpi / 25.4
    width = int(dpmm * c.paperWidth())
    height = int(dpmm * c.paperHeight())
    # create output image and initialize it
    image = QImage(QSize(width, height), QImage.Format_ARGB32)
    image.setDotsPerMeterX(dpmm * 1000)
    image.setDotsPerMeterY(dpmm * 1000)
    image.fill(0)

    # render the composition
    imagePainter = QPainter(image)
    sourceArea = QRectF(0,0, c.paperWidth(), c.paperHeight())
    targetArea = QRectF(0, 0, width, height)
    c.render(imagePainter, targetArea, sourceArea)
    imagePainter.end()
    image.save('C:\\Temp\\'+ name +'.jpg',"jpg")

def myfun():
    global cx, cy, rx, ry, dd, isDone
    
    print("do somthing")
    doSomething( str(cx) + "_" + str(cy))
    
    if (cx+dd) not in rx:
        if(cy+dd) not in ry:
            isDone = True
        else:
            cy = cy+dd
            cx = rx[0]
    else:
        cx = cx+dd
    if not isDone:
        zoom2area(mycvs, cx, cy, dd)
    else:
        mycvs.mapCanvasRefreshed.disconnect(myfun)


mycvs.mapCanvasRefreshed.connect(myfun)


def zoom2area(canvas, x, y, d):
    canvas.setExtent(
            QgsRectangle(
                x, y, x+d, y+d
                ))
    canvas.refresh()
    print("zoom to : ", x, y, x+d, y+d)

zoom2area(mycvs, cx, cy, dd)