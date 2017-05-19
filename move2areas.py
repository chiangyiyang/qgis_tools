from qgis.utils import iface

rx = range(121,123)
ry = range(22,24)
cx = 121
cy = 22
dd = 1
isDone = False

mycvs = iface.mapCanvas()

def myfun():
    print("do somthing")
    global cx, cy, rx, ry, dd, isDone, myfun
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
