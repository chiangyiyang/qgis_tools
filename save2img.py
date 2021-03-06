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
    c.setPaperSize(w, h, False)
    composerMap = QgsComposerMap(c, 0, 0, w, h) 
    c.addItem(composerMap)

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
    sourceArea = QRectF(0, 0, w, h)
    targetArea = QRectF(0, 0, width, height)
    c.render(imagePainter, targetArea, sourceArea)
    imagePainter.end()
    image.save( name +'.' + type, type)
    print("Image '" + name + "' has been saved!")

captureImage(
            "./output/test22",      # file name
            "png",                  # file type
            100,                    # image dpi
            200,                    # image width
            200)                    # image height
