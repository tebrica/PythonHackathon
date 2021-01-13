from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui
import sys, random
from menu import UI

class CrazyCars(QMainWindow, UI):

    def __init__(self, parent=None):
        super(CrazyCars, self).__init__(parent)
        self.init()
        self.initUI()
        self.btn1.clicked.connect(self.openGame)
        self.btn2.clicked.connect(self.openInstructions)
        self.btn3.clicked.connect(self.openHighScore)


    def initUI(self):

        self.setGeometry(0,0,1200,850) #podesavanje prozora
        self.setWindowIcon(QIcon('cc.jpg'))
        self.setWindowTitle('Crazy Cars')
        self.setFixedSize(1200, 850)
        self.setCentralWidget(self.StackedWidgets)
        UI.center(self)

        self.show()

    def display(self):
       self.stackedWidgets.setCurrentIndex(3)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure you want to quit?", QMessageBox.Yes |  QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def openGame(self):
        self.StackedWidgets.setCurrentIndex(1)

    def openInstructions(self):
        print("")

    def openHighScore(self):
        sys.exit()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ig = CrazyCars()
    sys.exit(app.exec_())