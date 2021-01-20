from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random

from Game import Game


class UI(QtWidgets.QWidget):

    def init(self):
        self.StackedWidgets = QStackedWidget()
        self.home = QWidget()

        self.MenuUI()
        self.game = Game()

        self.StackedWidgets.addWidget(self.home)
        self.StackedWidgets.addWidget(self.game)


    def MenuUI(self):
        self.home.setFixedSize(1200, 850)

        layout = QHBoxLayout()

        oImage = QImage("Slike/background.png")
        sImage = oImage.scaled(QSize(1200, 850))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.btn1 = QPushButton('Play', self.home)
        self.btn2 = QPushButton('Instructions', self.home)
        self.btn3 = QPushButton('High Score', self.home)

        self.btn1.setFixedSize(200, 80)
        self.btn2.setFixedSize(200, 80)
        self.btn3.setFixedSize(200, 80)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.home.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



