import sys
import Object
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

PLAYER_SPEED            = 10
FRAME_TIME_MS           = 16  # ms/frame

class Player(QLabel, QGraphicsPixmapItem):

    def __init__(self, parent, KeyLeft, KeyRight, KeyUp, KeyDown, pic, picl, picr, x, y) :

        super(Player, self).__init__(parent)

        player = QPixmap(pic)
        self.dimX = 120
        self.dimY = 190
        self.left = KeyLeft
        self.right = KeyRight
        self.up = KeyUp
        self.down = KeyDown
        self.pic = pic
        self.picl = picl
        self.picr = picr
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.setGeometry(x, y, self.dimX, self.dimY)


    def game_update(self, keys_pressed):
        dx = 0
        dy = 0

        player = QPixmap(self.pic)
        self.setPixmap(player.scaled(self.dimX, self.dimY))

        if self.left in keys_pressed:
            dx -= PLAYER_SPEED
            player = QPixmap(self.picl)
            self.setPixmap(player.scaled(self.dimX, self.dimY))
        if self.right in keys_pressed:
            dx += PLAYER_SPEED
            player = QPixmap(self.picr)
            self.setPixmap(player.scaled(self.dimX, self.dimY))
        if self.up in keys_pressed:
            dy -= PLAYER_SPEED
        if self.down in keys_pressed:
            dy += PLAYER_SPEED
        self.setGeometry(self.x()+dx, self.y()+dy, self.dimX, self.dimY)

