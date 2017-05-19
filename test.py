from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.utils import iface


def captureImage(name, type, dpi, w, h):
    ##Output using Map Composer#########
    # set up composition
    mapRenderer = iface.mapCanvas().mapRenderer()
    c = QgsComposition(mapRenderer)
    c.setPlotStyle(QgsComposition.Print)
    c.setPrintResolution(dpi)
    

    # add a map to the composition
    x, y = 0,0
    #w, h = c.paperWidth(), c.paperHeight()
    #w, h = 50, 50
    c.setPaperSize(w, h, False)
    composerMap = QgsComposerMap(c, x, y, w, h) 
    c.addItem(composerMap)
    #c.resizePageToContents()

    ##Output to a raster image#########
    dpi = c.printResolution()
    dpmm = dpi / 25.4
    width = int(dpmm * w)
    height = int(dpmm * h)
    
    # create output image and initialize it
    image = QImage(QSize(width, height), QImage.Format_ARGB32)
    image.setDotsPerMeterX(dpmm * 1000)
    image.setDotsPerMeterY(dpmm * 1000)
    image.fill(0)

    # render the composition
    imagePainter = QPainter(image)
    sourceArea = QRectF(0,0, w, h)
    targetArea = QRectF(0, 0, width, height)
    c.render(imagePainter, targetArea, sourceArea)
    imagePainter.end()
    image.save( name +'.' + type, type)
    print("Image '" + name + "' has been saved!")

captureImage("./output/test04", "png", 100, 200, 200)
