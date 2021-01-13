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

SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850
PLAYER_Object_X_OFFSETS = [0,45]
PLAYER_Object_Y         = 15
Object_SPEED            = 6 # pix/frame
ObjectCar_SPEED            = 3 # pix/frame
ObjectCar_FRAMES           = 360
FRAME_TIME_MS           = 16  # ms/frame
import random


class ObjectCar1(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar1, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = True
        player = QPixmap("car_blue.png")
        self.dimX = 90
        self.dimY = 160
        self.setPixmap(player.scaled(self.dimX, self.dimY))

    def game_update(self):

        if not self.active:
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
            self.active = True
        if self.active:
            self.setGeometry(self.x(), self.y() + Object_SPEED, self.dimX, self.dimY)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)


class ObjectCar2(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar2, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = True
        player = QPixmap("car_yellow.png")
        self.dimX = 90
        self.dimY = 160
        self.setPixmap(player.scaled(self.dimX, self.dimY))

    def game_update(self):
        if not self.active:
            self.active = True
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
        else:
            self.setGeometry(self.x(), self.y() + ObjectCar_SPEED, self.dimX, self.dimY)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)

class ObjectCar3(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar3, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = True
        player = QPixmap("car_orange.png")
        self.dimX = 90
        self.dimY = 160
        self.setPixmap(player.scaled(self.dimX, self.dimY))

    def game_update(self):
        if not self.active:
            self.active = True
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
        else:
            self.setGeometry(self.x(), self.y() + ObjectCar_SPEED, self.dimX, self.dimY)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)

class ObjectCar4(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar4, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = True
        player = QPixmap("car_green.png")
        self.dimX = 90
        self.dimY = 160
        self.setPixmap(player.scaled(self.dimX, self.dimY))

    def game_update(self):
        if not self.active:
            self.active = True
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
        else:
            self.setGeometry(self.x(), self.y() + ObjectCar_SPEED, self.dimX, self.dimY)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)
