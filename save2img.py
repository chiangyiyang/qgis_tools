from PyQt4.QtCore import *
from qgis.utils import iface

mapRenderer = iface.mapCanvas().mapRenderer()
c = QgsComposition(mapRenderer)


c.setPlotStyle(QgsComposition.Print)
dpi = c.printResolution()
dpmm = dpi / 25.4
width = int(dpmm * c.paperWidth())
height = int(dpmm * c.paperHeight())
x, y = 0, 0
w, h = c.paperWidth(), c.paperHeight()

c.setPaperSize(500, 250)
c.setPrintResolution(72)
composerMap = QgsComposerMap(c, x ,y, w, h)
c.addItem(composerMap)

image = QImage(QSize(width, height), QImage.Format_ARGB32)
image.setDotsPerMeterX(dpmm * 1000)
image.setDotsPerMeterY(dpmm * 1000)
image.fill(0)
imagePainter = QPainter(image)
c.renderPage(imagePainter, 0 )

image.save("/home/user/test.png", "png")
imagePainter.end()
