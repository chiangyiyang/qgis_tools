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

# create image
img = QImage(QSize(5000, 5000), QImage.Format_ARGB32_Premultiplied)

# set image's background color
color = QColor(255, 255, 0)
img.fill(color.rgb())

# create painter
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)


mapCanvas = iface.mapCanvas()
pts = [[13496849.583491117,13427468.542009214,12978182.73213968]
,[2882698.3315221076,2785696.282111045,4877589.175822471]]

x=pts[0][0]
y=pts[1][0]
width=5000
height=5000
#zoom2area(
#    mapCanvas, 
#    x, y,
#    width, height)
    
render = QgsMapRenderer()

# set layer set
layer = iface.activeLayer()
lst = [layer.id()]  # add ID of every layer
render.setLayerSet(lst)

# set extent
#rect = QgsRectangle(render.fullExtent())
#rect.scale(1.1)
#render.setExtent(rect)

render.setExtent(QgsRectangle(
                x - width/2, y - height/2, 
                x + width/2, y + height/2
                ))

# set output size
render.setOutputSize(img.size(), img.logicalDpiX())

# do the rendering
render.render(p)

p.end()

# save image
img.save("./output/render.png","png")