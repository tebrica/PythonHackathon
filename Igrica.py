from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui
import sys, random, os
from menu import UI
from Game import Game

class CrazyCars(QMainWindow, UI):

    def __init__(self, parent=None): #Batman vibes
        super(CrazyCars, self).__init__(parent)
        self.init()
        self.initUI()
        self.btn1.clicked.connect(self.openGame)
        self.btn2.clicked.connect(self.openInstructions)


    def initUI(self):

        self.setGeometry(0,0,1200,850) #podesavanje prozora
        self.setWindowIcon(QIcon('Slike/cc.jpg'))
        self.setWindowTitle('Crazy Cars')
        self.setFixedSize(1200, 850)
        self.setCentralWidget(self.StackedWidgets)
        UI.center(self)

        self.show()

    def display(self):
       self.stackedWidgets.setCurrentIndex(2)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?", QMessageBox.Yes |  QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            os.kill()

        else:
            event.ignore()

    def openGame(self):
        self.SetGame()

    def openInstructions(self):
        self.StackedWidgets.setCurrentIndex(1)
        self.StackedWidgets.setGeometry(160, 50, 700, 900)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ig = CrazyCars()
    sys.exit(app.exec_())