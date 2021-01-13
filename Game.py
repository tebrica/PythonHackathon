import sys
import Car
import Object
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFrame, QLabel, QWidget
from PyQt5.QtGui import QBrush, QImage, QPalette, QIcon, QPixmap
from PyQt5.QtCore import *
from multiprocessing import Process, Pipe, Queue
from threading import Thread
import time, random

from PyQt5.QtCore import (
    Qt,
    QThread,
    QBasicTimer,
    QSize,
    QPointF
)
from PyQt5.QtGui import (
    QBrush,
    QPixmap,
    QImage,
    QPalette
)
from PyQt5.QtWidgets import (
    QFrame,
    QApplication,
    QGraphicsItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView
)

#board = igra()
class Game(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.board = igra(self)
        self.setCentralWidget(self.board)
        self.resize(1200, 850)
        self.center()
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon("cc.jpg"))

        # setting background picture
        oImage = QImage("bck.jpg")
        sImage = oImage.scaled(1200, 850)
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.show()

    # method for centering main window
    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850
FRAME_TIME_MS           = 16  # ms/frame

class igra(QFrame, QGraphicsScene):

    def __init__(self, parent):
        super().__init__(parent)
        self.init_board()

    def init_board(self):
        #dva igraca


        self.player= Car.Player(self, Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down, "player1.png", "player1_left.png",
                                 "player1_right.png", (SCREEN_WIDTH / 2) + 200, ((SCREEN_HEIGHT) - 250), 'Igrac1')
        self.player1 = Car.Player(self, Qt.Key_A, Qt.Key_D, Qt.Key_W, Qt.Key_S, "player2.png", "player2_left.png",
                                  "player2_right.png",(SCREEN_WIDTH / 2 )-200,((SCREEN_HEIGHT) - 250), 'Igrac2')

        self.Objects = [Object.Object(self, 150, 365),
                        Object.Object(self, 365, 580),
                        Object.Object(self, 580, 795),
                        Object.Object(self, 700, 900),
                        Object.Object(self, 500, 800),
                        Object.Object(self, 200, 500),
                        Object.ObjectCar(self, 150, 580),
                        Object.ObjectCar(self, 580, 900),
                        Object.ObjectCar(self, 150, 580),
                        Object.ObjectCar(self, 580, 900)]

        self.players = [self.player, self.player1]

        #self.upProc = updateProcess()
        #self.upProc.start()
        #self.threadingCheck(self.player1)
        #self.startProcess()                        #PROCES

        self.keys_pressed = set()
        self.setFocusPolicy(Qt.StrongFocus)
        #self.timer = QBasicTimer()                 #TIMER
        #self.timer.start(FRAME_TIME_MS, self)      #TIMER

        self.Qt1 = QThread()
        self.moveToThread(self.Qt1)
        self.Qt1.started.connect(self.game_update)
        self.Qt1.start()

        self.threadingCheck(self.player)
        #self.threadingCheck(self.player1) ZA PLAYERA 2

        #proc = updateProcess()
        #proc.start()
        #proc1 = updateProcess1()
        #proc1.start()

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def worker(self):
        for player in self.players:
            self.check(player)


    def check(self, player):

        while True:
            for b in self.Objects:
                if player.x() in range(b.x()-50, b.x()+50):
                    if player.y() in range(b.y()-50, b.y()+50):
                        player.health = player.health-1
                        if player.health < 0:
                            print(f'{player.name} nea vise elta :(')
                            return
                        print(f'{player.name} helti:{player.health}')
                        t_end = time.time() + 2
                        while time.time() < t_end:
                            player.setGeometry(player.x()-3000,player.y()-3000, player.dimX, player.dimY)
                            time.sleep(0.25)
                            player.setGeometry(player.x()+3000, player.y()+3000, player.dimX, player.dimY)
                            time.sleep(0.25)
                        break

    def game_update(self):
        while True:
            if self.player1.health >= 0:
                self.player1.game_update(self.keys_pressed)
            if self.player.health >= 0:
                self.player.game_update(self.keys_pressed)
            for b in self.Objects:
                b.game_update()
            QApplication.processEvents()
            time.sleep(0.015)

    def threadingCheck(self, player:Car.Player):

        self.t1 = Thread(target=self.check, args=(player,))
        self.t1.start()
