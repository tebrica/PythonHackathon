from multiprocessing import Process
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
from PyQt5.QtWidgets import QLabel
import time

SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850
PLAYER_Object_X_OFFSETS = [0,45]
PLAYER_Object_Y         = 15
Object_SPEED            = 10 # pix/frame
ObjectCar_SPEED            = 5 # pix/frame
ObjectCar_FRAMES           = 360
FRAME_TIME_MS           = 16  # ms/frame
import random



class Object(QLabel):
    def __init__(self, parent, x, y):

        super(Object, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = True
        player = QPixmap("Obstacle.png")
        self.dimX = 100
        self.dimY = 100
        self.setPixmap(player.scaled(self.dimX, self.dimY))

    def game_update(self):
        if not self.active:
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-1300, -100), self.dimX,
                             self.dimY)
            self.active = True
        if self.active:
            self.setGeometry(self.x(), self.y() + Object_SPEED, self.dimX, self.dimY)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)


class ObjectCar(QLabel):
    def __init__(self, parent, x, y):

        super(ObjectCar, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = True
        player = QPixmap("Obstacle1.png")
        self.dimX = 150
        self.dimY = 250
        self.setPixmap(player.scaled(self.dimX, self.dimY))


    def game_update(self):
        if not self.active:
            self.active = True
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-1300, -100), self.dimX, self.dimY)
        else:
            self.setGeometry(self.x(), self.y() + ObjectCar_SPEED, self.dimX, self.dimY)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)
