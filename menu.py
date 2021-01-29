import winsound

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, QRect
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, random
from Game import Game
from GameOverScreen import GameOverScreen

class UI(QtWidgets.QWidget):

    def init(self):
        name = 'Sound/Home.wav'
        winsound.PlaySound(name, winsound.SND_ASYNC)
        self.i = 2
        self.StackedWidgets = QStackedWidget()
        self.home = QWidget()

        #Turnir
        self.winners = None
        self.currentPlayer = 0
        self.lastChoice = None
        self.turnirUToku = False
        self.activePair = None

        self.MenuUI()
        self.gameOverScreen = GameOverScreen(self)
        self.gameOverScreen.buttonRet.clicked.connect(lambda: self.gameOverScreen.returnHome(self.StackedWidgets))

        self.instructions = Instructions()
        self.instructions.buttonRet.clicked.connect(lambda: self.instructions.returnHome(self.StackedWidgets))

        self.StackedWidgets.addWidget(self.home)
        self.StackedWidgets.addWidget(self.instructions)
        self.StackedWidgets.addWidget(self.gameOverScreen)

    def SetGame(self):
        self.turnirUToku = True
        self.activePair = self.pairs[self.currentPlayer]
        self.i = self.i +1
        print("Set game pair: " + str(self.pairs[self.currentPlayer]) )

        self.game = Game(self.StackedWidgets, self.gameOverScreen, self.pairs[self.currentPlayer], self)
        self.StackedWidgets.addWidget(self.game)
        self.StackedWidgets.setCurrentIndex(self.i)

    def getWinner(self, playerWinner):
        self.prayers = None
        print("--------GetWinner-----------")
        print ("Winner is: " + playerWinner)
        if self.winners == None:
            self.currentPlayer = 1
            self.winners = [None] * int(self.igraci/2)
            #print("Broj igraca winners: " + str(len(self.winners)))
        else:
            self.currentPlayer += 1
        self.winners[self.currentPlayer - 1] = playerWinner

        print("--------Winners list----------")
        print(self.winners)
        print("--------############----------")

        if self.currentPlayer == int(self.igraci/2):
            if self.currentPlayer == 1:
                print("Pobednik turnira je:" + playerWinner)
                self.turnirUToku = False
                self.currentPlayer = 0
                self.players = None
                self.winners = None
                self.igraci = self.lastChoice
                self.makeBracket()
                return

            self.prayers = self.winners
            self.igraci = self.igraci / 2
            self.winners = None
            self.currentPlayer = 0
            self.makePairs()

    def MenuUI(self):
        self.home.setFixedSize(1200, 850)

        layout = QHBoxLayout()
        oImage = QImage("Slike/background.png")
        sImage = oImage.scaled(QSize(1200, 928))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.combo = QComboBox(self)
        self.igraci = 2
        self.lastChoice = 2
        self.combo.addItem("2 players")
        self.makeBracket()
        self.combo.addItem("4 players")
        self.combo.addItem("8 players")
        self.combo.activated[str].connect(self.selectionchange)
        layout.addWidget(self.combo)

        self.btn1 = QPushButton('Play', self.home)
        self.btn2 = QPushButton('Instructions', self.home)

        self.btn1.setFixedSize(200, 80)
        self.btn2.setFixedSize(200, 80)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.home.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def selectionchange(self, text):
        if text == "2 players":
            self.igraci = 2
        elif text == "4 players":
            self.igraci = 4
        else:
            self.igraci = 8

        self.makeBracket()

    def makeBracket(self):
        self.pairs = []
        if self.igraci == 2:
            self.prayers = ["Igrac 1", "Igrac 2"]
        elif self.igraci == 4:
            self.prayers = ["Igrac 1", "Igrac 2", "Igrac 3", "Igrac 4"]
        elif self.igraci == 8:
            self.prayers = ["Igrac 1", "Igrac 2", "Igrac 3", "Igrac 4", "Igrac 5", "Igrac 6", "Igrac 7", "Igrac 8"]

        print("--------MAKE Bracket-----------")
        self.lastChoice = self.igraci
        self.makePairs()
        print("-------------------------------")

    def makePairs(self):
        while self.prayers:
            rand1 = self.pop_random()
            rand2 = self.pop_random()
            pair = rand1, rand2
            print("Par: " + pair[0] + " | " + pair[1])
            self.pairs.append(pair)

    def pop_random(self):
        idx = random.randrange(0, len(self.prayers))
        return self.prayers.pop(idx)

class Instructions(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(900, 700)

        self.setStyleSheet("background-image: url(Slike/instructions.png)")

        self.buttonRet = QPushButton('',self)
        self.buttonRet.setFixedSize(517, 630)

        layout = QHBoxLayout()

        layout.addWidget(self.buttonRet)
        layout.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(layout)


    def returnHome(self, sw):
        sw.setCurrentIndex(0)














































































































































































































































































































































