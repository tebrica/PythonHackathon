import sys
from multiprocessing.dummy import Process

import Object
from PyQt5.QtCore import (
    Qt,
    QBasicTimer,
    QSize,
    QPointF, QThread
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

PLAYER_SPEED            = 12
FRAME_TIME_MS           = 16  # ms/frame
SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850

class Player(QLabel):

    def __init__(self, parent, KeyLeft, KeyRight, KeyUp, KeyDown, pic, picl, picr, x, y, name) :

        super(Player, self).__init__(parent)
        self.name = name
        self.health = 3
        self.dimX = 90
        self.dimY = 170
        self.left = KeyLeft
        self.right = KeyRight
        self.up = KeyUp
        self.down = KeyDown
        self.pic = pic
        self.picl = picl
        self.picr = picr
        player = QPixmap(pic)
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.setGeometry(x, y, self.dimX, self.dimY)

    def game_update(self, keys_pressed):
        dx = 0
        dy = 0

        player = QPixmap(self.pic)
        self.setPixmap(player.scaled(self.dimX, self.dimY))

        if self.left in keys_pressed:
            if self.x() > 150:
                dx -= PLAYER_SPEED
                player = QPixmap(self.picl)
                self.setPixmap(player.scaled(self.dimX, self.dimY))
        if self.right in keys_pressed:
            if self.x() < SCREEN_WIDTH-250:
                dx += PLAYER_SPEED
                player = QPixmap(self.picr)
                self.setPixmap(player.scaled(self.dimX, self.dimY))
        if self.up in keys_pressed:
            if self.y() > 100:
                dy -= PLAYER_SPEED
        if self.down in keys_pressed:
            if self.y() < SCREEN_HEIGHT-200:
                dy += PLAYER_SPEED
        self.setGeometry(self.x()+dx, self.y()+dy, self.dimX, self.dimY)

