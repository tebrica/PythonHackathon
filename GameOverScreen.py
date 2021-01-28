from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import sys, random
import winsound
class GameOverScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setFixedSize(1280, 960)

        self.setStyleSheet("background-image: url(Slike/instructions.png)")

        self.buttonRet = QPushButton('',self)
        self.buttonRet.setFixedSize(640, 480)

        layout = QHBoxLayout()
        
        layout.addWidget(self.buttonRet)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(layout)


    def returnHome(self, sw):
        if self.parent.turnirUToku:
            self.parent.SetGame()
        else:
            sw.setCurrentIndex(0)

    def changeWinner(self, id, ):
        if(id == 1):

            self.setStyleSheet("background-image: url(Slike/player1win.png)")

            self.winnerName = self.parent.activePair[1]
            self.labelA = QLabel(self)
            self.labelA.setText("Winner is: " + self.winnerName)
            self.labelA.setFixedWidth(500)
            self.labelA.setFixedHeight(70)
            self.labelA.setAlignment(QtCore.Qt.AlignCenter)
            self.labelA.move(390, 380)
            self.labelA.setFont(QFont("Arial", 40))
            self.labelA.setStyleSheet("QLabel{background-color: white; color: black; font-weight: bold;}")
            self.labelA.raise_()
        else:

            self.setStyleSheet("background-image: url(Slike/player1win.png)")

            self.winnerName = self.parent.activePair[0]
            self.labelA = QLabel(self)
            self.labelA.setText("Winner is: " + self.winnerName)
            self.labelA.setFixedWidth(500)
            self.labelA.setFixedHeight(70)
            self.labelA.setAlignment(QtCore.Qt.AlignCenter)
            self.labelA.move(390, 380)
            self.labelA.setFont(QFont("Arial", 40))
            self.labelA.setStyleSheet("QLabel{background-color: white; color: black; font-weight: bold;}")
            self.labelA.raise_()

        name = 'Sound/GameOver.wav'
        winsound.PlaySound(name, winsound.SND_ASYNC)