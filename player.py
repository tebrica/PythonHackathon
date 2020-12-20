from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap


class Player(QLabel):

    def __init__(self, parent, x, y, pic):
        super(Player, self).__init__(parent)

        self.dimX = 120
        self.dimY = 160
        player = QPixmap(pic)
        self.setPixmap(player.scaled(self.dimX, self.dimY))
        player = player.scaled(self.dimX, self.dimY)
        self.x = x
        self.y = y
        self.setGeometry(x, y, self.dimX, self.dimY)
