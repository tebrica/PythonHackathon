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

PLAYER_SPEED            = 5
FRAME_TIME_MS           = 16  # ms/frame
SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850

PLAYER_SPEED_WHEN_HIT   = 3

class Player(QLabel, QGraphicsPixmapItem):

    def __init__(self, parent, KeyLeft, KeyRight, KeyUp, KeyDown, pic, picl, picr, x, y) :

        super(Player, self).__init__(parent)
        self.speedHit = 3
        self.speedSlow = False
        self.dimX = 90
        self.dimY = 170
        self.left = KeyLeft
        self.right = KeyRight
        self.up = KeyUp
        self.down = KeyDown
        self.pic = pic
        self.picl = picl
        self.picr = picr
        self.player = QPixmap(pic)
        self.setPixmap(self.player.scaled(self.dimX, self.dimY))
        self.setGeometry(x, y, self.dimX, self.dimY)
        self.untouchable = False

    def game_update(self, keys_pressed):
        dx = 0
        dy = 0

        if self.speedSlow == True:
            PLAYER_SPEED = 2
        else:
            PLAYER_SPEED = 5
        #if newX < Board.BoardWidth - 330 and newX > 220:

        if self.up in keys_pressed:
            if self.y() > 100:
                dy -= PLAYER_SPEED
                self.player = QPixmap(self.pic)
        elif self.down in keys_pressed:
            if self.y() < SCREEN_HEIGHT-200:
                dy += PLAYER_SPEED
                self.player = QPixmap(self.pic)
        elif self.right in keys_pressed:
            if self.x() < SCREEN_WIDTH-250:
                dx += PLAYER_SPEED
                self.player = QPixmap(self.picr)
                self.setPixmap(self.player.scaled(self.dimX, self.dimY))
        elif self.left in keys_pressed:
            if self.x() > 150:
                dx -= PLAYER_SPEED
                self.player = QPixmap(self.picl)
                self.setPixmap(self.player.scaled(self.dimX, self.dimY))
        else:
            self.player = QPixmap(self.pic)

        self.setGeometry(self.x()+dx, self.y()+dy, self.dimX, self.dimY)
        self.setPixmap(self.player.scaled(self.dimX, self.dimY))

