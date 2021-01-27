from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QLabel, QGraphicsPixmapItem
from Car import Player

class highscore(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y, player: Player):

        super(highscore, self).__init__(parent)
        self.labelA = QLabel(parent)
        self.labelA.setText("0")
        self.labelA.move(x, y)
        self.labelA.setFont(QFont("Arial", 20))
        self.labelA.setStyleSheet("QLabel{background-color:white; color: black;}")
        self.labelA.setAlignment(Qt.AlignCenter)
        self.parent = parent
        self.player = player
        self.health = 3
        self.dimX = 150
        self.dimY = 150

    def scoreUpdate(self, score):

        self.labelA.setText(score)

