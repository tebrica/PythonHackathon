from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random

class GameOverScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1280,960)

        self.setStyleSheet("background-image: url(Slike/instructions.png)")

        self.buttonRet = QPushButton('',self)
        self.buttonRet.setFixedSize(640, 480)

        layout = QHBoxLayout()
        
        layout.addWidget(self.buttonRet)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(layout)



    def returnHome(self, sw):
        sw.setCurrentIndex(0)

    def changeWinner(self, id):
        if(id == 1):
            self.setStyleSheet("background-image: url(Slike/player2win.png)")
        else:
            self.setStyleSheet("background-image: url(Slike/player1win.png)")