from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QLabel, QGraphicsPixmapItem
from Car import Player

class highscore(QLabel, QGraphicsPixmapItem):
    def __init__(self, parent, x, y, player: Player):

        super(highscore, self).__init__(parent)

        self.x = x
        self.y = y
        self.parent = parent
        self.player = player
        self.dimX = 150
        self.dimY = 150

        self.labelA = QLabel(self.parent)
        self.labelA.setText("0")
        self.labelA.setFixedWidth(120)
        self.labelA.move(self.x, self.y)
        self.labelA.setFont(QFont("Arial", 20))
        self.labelA.setStyleSheet("QLabel{background-color:white; color: black;}")
        self.labelA.setAlignment(Qt.AlignCenter)

    def scoreUpdate(self, score):
        self.labelA.setText(score)
