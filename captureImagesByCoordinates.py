from qgis.utils import iface
from PyQt4.QtCore import *
from PyQt4.QtGui import *

a=[13496849.583491117,13427468.542009214,12978182.73213968]
b=[2882698.3315221076,2785696.282111045,4877589.175822471]
inx = 0
cx = 0
cy = 0
imgWidth = 10000
imgHeight = 10000
isDone = False

mycvs = iface.mapCanvas()

def captureImage(name):
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
    image.save('./output/'+ name +'.jpg',"jpg")

def doNext():
    global cx, cy, isDone, inx, a, b
    
    print("CaptureImage")
    captureImage( str(cx) + "_" + str(cy))
    
    if inx >= len(a):
        isDone = True
    else:
        cx = a[inx]
        cy = b[inx]
        inx += 1
    
    if not isDone:
        zoom2area(mycvs, cx, cy)
    else:
        mycvs.mapCanvasRefreshed.disconnect(doNext)
        print("All Done!! :)")

mycvs.mapCanvasRefreshed.connect(doNext)

def zoom2area(canvas, x, y):
    global imgWidth, imgHeight
    canvas.setExtent(
            QgsRectangle(
                x - imgWidth/2, y - imgHeight/2, 
                x + imgWidth/2, y + imgHeight/2
                ))
    canvas.refresh()
    print("zoom to : ", x, y, x+imgWidth, y+imgHeight)

zoom2area(mycvs, cx, cy)