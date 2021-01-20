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
Object_SPEED            = 5 # pix/frame
ObjectCar_SPEED            = 2 # pix/frame
ObjectCar_FRAMES           = 360
FRAME_TIME_MS           = 16  # ms/frame
import random


class ObjectCar1(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar1, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = False
        player = QPixmap("Slike/car_blue.png")
        self.dimX = 90
        self.dimY = 170
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.player = parent.player
        self.player1 = parent.player1



    def game_update(self):

        if not self.active:
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
            self.active = True
        if self.active:
            self.setGeometry(self.x(), self.y() + Object_SPEED, self.dimX, self.dimY)
            #kontakt plavog igraca i auta
            self.pozicijaPlayer = self.player.geometry()
            if(self.player.x() < self.x() + 85 and self.player.x() + 85 > self.x()) and\
                    (self.player.y() +160 > self.y() and self.player.y() < self.y() + 160):
                self.player.setGeometry(800, 600, 90, 170)
            # kontakt crvenog igraca i auta
            self.pozicijaPlayer1 = self.player1.geometry()
            if (self.player1.x() < self.x() + 85 and self.player1.x() + 85 > self.x()) and \
                    (self.player1.y() + 160 > self.y() and self.player1.y() < self.y() + 160):
                self.player1.setGeometry(400, 600, 90, 170)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)


class ObjectCar2(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar2, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = False
        player = QPixmap("Slike/car_yellow.png")
        self.dimX = 90
        self.dimY = 160
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.player = parent.player
        self.player1 = parent.player1


    def game_update(self):

        if not self.active:
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
            self.active = True
        if self.active:
            self.setGeometry(self.x(), self.y() + Object_SPEED, self.dimX, self.dimY)
            # kontakt plavog igraca i auta
            self.pozicijaPlayer = self.player.geometry()
            if (self.player.x() < self.x() + 85 and self.player.x() + 85 > self.x()) and \
                    (self.player.y() + 160 > self.y() and self.player.y() < self.y() + 160):
                self.player.setGeometry(800, 600, 90, 170)
            # kontakt crvenog igraca i auta
            self.pozicijaPlayer1 = self.player1.geometry()
            if (self.player1.x() < self.x() + 85 and self.player1.x() + 85 > self.x()) and \
                    (self.player1.y() + 160 > self.y() and self.player1.y() < self.y() + 160):
                self.player1.setGeometry(400, 600, 90, 170)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)

class ObjectCar3(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar3, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = False
        player = QPixmap("Slike/prepreka1.png")
        self.dimX = 90
        self.dimY = 90
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.player = parent.player
        self.player1 = parent.player1

    def game_update(self):
        if not self.active:
            self.active = True
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
        else:
            self.setGeometry(self.x(), self.y() + ObjectCar_SPEED, self.dimX, self.dimY)
            # kontakt plavog igraca i prepreke
            self.pozicijaPlayer = self.player.geometry()
            if (self.player.x() < self.x() + 45 and self.player.x() + 45 > self.x()) and \
                    (self.player.y() + 45 > self.y() and self.player.y() < self.y() + 45):
                self.player.setGeometry(800, 600, 90, 170)
            # kontakt crvenog igraca i prepreke
            self.pozicijaPlayer1 = self.player1.geometry()
            if (self.player1.x() < self.x() + 45 and self.player1.x() + 45 > self.x()) and \
                    (self.player1.y() + 45 > self.y() and self.player1.y() < self.y() + 45):
                self.player1.setGeometry(400, 600, 90, 170)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)

class ObjectCar4(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y):

        super(ObjectCar4, self).__init__(parent)
        self.xPos = x
        self.yPos = y
        self.active = False
        player = QPixmap("Slike/prepreka2.png")
        self.dimX = 90
        self.dimY = 90
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.player = parent.player
        self.player1 = parent.player1

    def game_update(self):
        if not self.active:
            self.active = True
            self.setGeometry(random.randrange(self.xPos, self.yPos), random.randrange(-450, -100), self.dimX, self.dimY)
        else:
            self.setGeometry(self.x(), self.y() + ObjectCar_SPEED, self.dimX, self.dimY)
            # kontakt plavog igraca i prepreke
            self.pozicijaPlayer = self.player.geometry()
            if (self.player.x() < self.x() + 45 and self.player.x() + 45 > self.x()) and \
                    (self.player.y() + 45 > self.y() and self.player.y() < self.y() + 45):
                self.player.setGeometry(800, 600, 90, 170)
            # kontakt crvenog igraca i prepreke
            self.pozicijaPlayer1 = self.player1.geometry()
            if (self.player1.x() < self.x() + 45 and self.player1.x() + 45 > self.x()) and \
                    (self.player1.y() + 45 > self.y() and self.player1.y() < self.y() + 45):
                self.player1.setGeometry(400, 600, 90, 170)
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)
