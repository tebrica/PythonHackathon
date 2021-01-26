from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QGraphicsPixmapItem

Background_SPEED = 2

class background(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, y):
        super(background, self).__init__(parent)

        self.parent = parent
        self.YPosition = y
        self.pic = "Slike/background.png"
        player = QPixmap(self.pic)
        self.dimX = 1200
        self.dimY = 928
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        self.setGeometry(0, self.YPosition, self.dimX, self.dimY)

    def update(self):
        if self.y() > 900:
            self.YPosition = -900
            self.setGeometry(0, self.YPosition, self.dimX, self.dimY)

        self.YPosition = self.YPosition + Background_SPEED
        self.setGeometry(0, self.YPosition, self.dimX, self.dimY)