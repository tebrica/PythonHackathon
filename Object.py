import time
from threading import Thread

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
    def __init__(self, parent, x, y, pic):

        super(ObjectCar1, self).__init__(parent)
        self.parent = parent
        self.xPos = x
        self.yPos = y
        self.active = False
        self.pic = pic
        player = QPixmap(self.pic)
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
                    (self.player.y() +160 > self.y() and self.player.y() < self.y() + 160 and not self.parent.player.untouchable):
                self.player.setGeometry(800, 600, 90, 170)
                self.parent.health.HealthLoss()
                if self.parent.player.untouchable:
                    return
                self.t = Thread(target=self.blink, args=(self.parent.player,))
                self.t.start()
            # kontakt crvenog igraca i auta
            self.pozicijaPlayer1 = self.player1.geometry()
            if (self.player1.x() < self.x() + 85 and self.player1.x() + 85 > self.x()) and \
                    (self.player1.y() + 160 > self.y() and self.player1.y() < self.y() + 160 and not self.parent.player1.untouchable):
                self.player1.setGeometry(400, 600, 90, 170)
                self.parent.health1.HealthLoss()
                if self.parent.player1.untouchable:
                    return
                self.t = Thread(target=self.blink, args=(self.parent.player1,))
                self.t.start()
            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)

    def blink(self, player):
        i = 0
        player.untouchable = True
        while (i < 8):
            player.dimX = 0
            player.dimY = 0
            time.sleep(0.15)
            player.dimX = 90
            player.dimY = 170
            time.sleep(0.15)
            i = i + 1
        player.untouchable = False



class ObjectCar3(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y, pic):

        super(ObjectCar3, self).__init__(parent)
        self.parent = parent
        self.xPos = x
        self.yPos = y
        self.active = False
        self.pic = pic
        player = QPixmap(self.pic)
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
                    (self.player.y() + 45 > self.y() and self.player.y() < self.y() + 45 and not self.parent.player.untouchable):
                self.player.setGeometry(800, 600, 90, 170)
                self.parent.health.HealthLoss()
                if self.parent.player.untouchable:
                    return
                self.t = Thread(target=self.blink, args=(self.parent.player,))
                self.t.start()
            # kontakt crvenog igraca i prepreke
            self.pozicijaPlayer1 = self.player1.geometry()
            if (self.player1.x() < self.x() + 45 and self.player1.x() + 45 > self.x()) and \
                    (self.player1.y() + 45 > self.y() and self.player1.y() < self.y() + 45 and not self.parent.player1.untouchable):
                self.player1.setGeometry(400, 600, 90, 170)
                self.parent.health1.HealthLoss()
                if self.parent.player1.untouchable:
                    return
                self.t = Thread(target=self.blink, args=(self.parent.player1,))
                self.t.start()

            if self.y() > 950:
                self.active = False
                self.setGeometry(SCREEN_WIDTH, SCREEN_HEIGHT, self.dimX, self.dimY)


    def blink(self, player):
        i = 0
        player.untouchable = True
        while(i < 8):
            player.dimX = 0
            player.dimY = 0
            time.sleep(0.15)
            player.dimX = 90
            player.dimY = 170
            time.sleep(0.15)
            i = i+1
        player.untouchable = False