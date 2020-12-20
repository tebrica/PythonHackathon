from PyQt5.QtCore import (
    Qt,
    QBasicTimer,
    QSize,
    QPointF
)
from PyQt5.QtGui import (
    QBrush,
    QPixmap,
    QImage,
    QPalette
)
from PyQt5.QtWidgets import (
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView
)

SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850
PLAYER_Object_X_OFFSETS = [0,45]
PLAYER_Object_Y         = 15
Object_SPEED            = 6 # pix/frame
Object_FRAMES           = 120
FRAME_TIME_MS           = 16  # ms/frame
import random

class Object(QGraphicsPixmapItem):
    def __init__(self, offset_x, offset_y, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Obstacle.png"))
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.active = False
        self.frames = 0

    def game_update(self):
        if not self.active:
                self.active = True
                self.setPos(random.randrange(100,1100), 50)
                self.frames = Object_FRAMES
        else:
            self.setPos(self.x(),self.y()+Object_SPEED)
            self.frames -= 1
            if self.frames <= 0:
                self.active = False
                self.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)

