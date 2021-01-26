from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QGraphicsPixmapItem
from Car import Player
from GameOverScreen import GameOverScreen

class health(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y, player: Player, sw, id, wm):

        super(health, self).__init__(parent)
        self.x = x
        self.y = y
        self.parent = parent
        self.player = player
        self.health = 3
        self.dimX = 150
        self.dimY = 150
        self.pic = QPixmap("Slike/Health.png")
        self.setPixmap(self.pic.scaled(self.dimX, self.dimY))
        self.setGeometry(x, y, self.dimX, self.dimY)
        self.sw = sw
        self.id = id
        self.winnerMenu = wm

    def HealthLoss(self):
        self.health = self.health-1
        self.dimX = self.dimX - 50
        self.dimY = self.dimY - 50
        self.x = self.x + 25
        self.y = self.y + 25
        self.setPixmap(self.pic.scaled(self.dimX, self.dimY))
        self.setGeometry(self.x, self.y, self.dimX, self.dimY)
        if self.health < 0:
            self.dimX = 0
            self.dimY = 0
            self.setPixmap(self.pic.scaled(0, 0))
            self.player.dimX = 0
            self.player.dimY = 0
            self.player.untouchable = True
            self.winnerMenu.changeWinner(self.id)
            self.sw.setCurrentIndex(2)