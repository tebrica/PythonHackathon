import sys
import threading
import Car
import Object
import health
import background
from highscore import highscore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFrame, QLabel, QWidget
from PyQt5.QtGui import QBrush, QImage, QPalette, QIcon, QPixmap
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from multiprocessing import Queue, Process, Pipe
import time, random
import multiprocessing as mp
from JobWorker import jobWorker
from PyQt5.QtCore import (
    QThread,
    Qt,
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

class Game(QMainWindow):

    def __init__(self, sw, wm, par , mec):
        super().__init__()
        self.sw = sw
        self.wm = wm
        self.player1 = par[0]
        self.player2 = par[1]
        self.mec = mec
        self.initUI()

    def initUI(self):
        self.board = igra(self, self.sw, self.wm, self.player1, self.player2)
        self.setCentralWidget(self.board)

        self.resize(1200, 850)
        self.center()
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon("Slike/cc.jpg"))

        self.show()

    # method for centering main window
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def vratiPobednika(self, playerWinner):
        self.mec.getWinner(playerWinner)


SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850
FRAME_TIME_MS           = 8  # ms/frame

class igra(QFrame, QGraphicsScene):

    def __init__(self, parent:Game, sw, wm, playerA, playerB):
        super().__init__(parent)
        self.playerA = playerA
        self.playerB = playerB
        self.sw = sw
        self.wm = wm
        self.parent = parent
        self.playerWinner = None
        self.init_board()

    def __del__(self):
        self.timer.stop()
        self.returnWinner()
        self = None


    def init_board(self):

        self.background1 = background.background(self, -889)
        self.background2 = background.background(self, 0)

        #dva igraca
        self.player = Car.Player(self, Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down, "Slike/player1.png", "Slike/player1_left.png",
                                 "Slike/player1_right.png", (SCREEN_WIDTH / 2) + 200, ((SCREEN_HEIGHT) - 250), self.playerA)
        self.player1 = Car.Player(self, Qt.Key_A, Qt.Key_D, Qt.Key_W, Qt.Key_S, "Slike/player2.png", "Slike/player2_left.png",
                                  "Slike/player2_right.png",(SCREEN_WIDTH / 2 )-200,((SCREEN_HEIGHT) - 250), self.playerB)

        self.health = health.health(self,1050,50, self.player, self.sw, 1, self.wm, "Slike/HeartLBlue.png" )
        self.health1 = health.health(self,0,50, self.player1, self.sw, 2, self.wm, "Slike/HeartRed.png" )

        self.Objects = [Object.ObjectCar3(self, 150, 580, "Slike/prepreka2.png"),
                        Object.ObjectCar3(self, 580, 900, "Slike/prepreka1.png"),
                        Object.ObjectCar1(self, 150, 580, "Slike/car_green.png"),
                        Object.ObjectCar1(self, 580, 900, "Slike/car_orange.png"),
                        Object.ObjectShield(self, 150, 580, "Slike/Shieldd.png")]

        self.highscore = highscore(self, 15, 15, self.player)
        self.highscore1 = highscore(self, 1065, 15, self.player1)

        #da se automobili prikazu preko prepreka
        self.player.raise_()
        self.player1.raise_()

        self.keys_pressed = set()
        self.setFocusPolicy(Qt.StrongFocus)
        self.initProcess()
        self.t = threading.Thread(target=self.initThreads, args=())
        self.t.start()
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)


    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        try: self.keys_pressed.remove(event.key())
        except:
            return

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.doJob()

    def initThreads(self):
        self.last = 0

        while True:
            data = self.ex_pipeHS.recv()
            data1 = self.ex_pipeHS1.recv()
            if data != None:
                self.highscore.scoreUpdate(data)
            if data1 != None:
                self.highscore1.scoreUpdate(data1)

            if int(data) % 100 == 0:
                for ob in self.Objects:
                    ob.speed = ob.speed + 1

                self.background1.speed += 1
                self.background2.speed += 1


    def initProcess(self):

        self.ex_pipe, self.in_pipe = mp.Pipe()
        self.ex_pipeHS, self.in_pipeHS = mp.Pipe()
        self.ex_pipeHS1, self.in_pipeHS1 = mp.Pipe()

        self.jw = jobWorker(self.in_pipe, self.in_pipeHS, self.in_pipeHS1)

        self.jw.start()

    def doJob(self):
        data = self.ex_pipe.recv()
        if data == "go":
            self.player1.game_update(self.keys_pressed)
            self.player.game_update(self.keys_pressed)
            self.background1.update()
            self.background2.update()

            for b in self.Objects:
               b.game_update()
        elif data == "stop":
            self.timer.stop()
            self.__del__()
        return

    def returnWinner(self):
        self.parent.vratiPobednika(self.playerWinner)
