import sys
import threading
import Car
import Object
import health
import background
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

    def __init__(self, sw, wm):
        super().__init__()
        self.sw = sw
        self.wm = wm
        self.initUI()

    def initUI(self):
        self.board = igra(self, self.sw, self.wm)
        self.setCentralWidget(self.board)

        self.resize(1200, 850)
        self.center()
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon("Slike/cc.jpg"))


        # setting background picture
        oImage = QImage("Slike/testBG.png")
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

    def __init__(self, parent, sw, wm):
        super().__init__(parent)

        self.sw = sw
        self.wm = wm
        self.init_board()

    def __del__(self):
        self.timer.stop()
        self = None

    def init_board(self):

        self.background1 = background.background(self, -928)
        self.background2 = background.background(self, 0)

        #dva igraca
        self.player = Car.Player(self, Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down, "Slike/player1.png", "Slike/player1_left.png",
                                 "Slike/player1_right.png", (SCREEN_WIDTH / 2) + 200, ((SCREEN_HEIGHT) - 250))
        self.player1 = Car.Player(self, Qt.Key_A, Qt.Key_D, Qt.Key_W, Qt.Key_S, "Slike/player2.png", "Slike/player2_left.png",
                                  "Slike/player2_right.png",(SCREEN_WIDTH / 2 )-200,((SCREEN_HEIGHT) - 250))

        self.health = health.health(self,1050,50, self.player, self.sw, 1, self.wm, "Slike/HeartLBlue.png" )
        self.health1 = health.health(self,0,50, self.player1, self.sw, 2, self.wm, "Slike/HeartRed.png" )

        self.Objects = [Object.ObjectCar3(self, 150, 580, "Slike/prepreka2.png"),
                        Object.ObjectCar3(self, 580, 900, "Slike/prepreka1.png"),
                        Object.ObjectCar1(self, 150, 580, "Slike/car_green.png"),
                        Object.ObjectCar1(self, 580, 900, "Slike/car_orange.png"),
                        Object.ObjectShield(self, 150, 580, "Slike/shield.png")]

        #da se automobili prikazu preko prepreka
        self.player.raise_()
        self.player1.raise_()

        self.keys_pressed = set()
        self.setFocusPolicy(Qt.StrongFocus)
        self.initProcess()
        #self.doJob()
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)
        #self.initThreads()

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.doJob()
        #self.player1.game_update(self.keys_pressed)
        #self.player.game_update(self.keys_pressed)
        #self.background1.update()
        #self.background2.update()

        #for b in self.Objects:
        #    b.game_update()


    def initThreads(self):
        self.initProcess()

        self.thread = QThread()
        self.worker = Worker(self.ex_pipe,self.player,self.keys_pressed, None, None)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.threadJobPlayer)
        self.thread.start()

        self.thread1 = QThread()
        self.worker1 = Worker(None, self.player1, self.keys_pressed, self.ex_pipe2, None)
        self.worker1.moveToThread(self.thread1)
        self.thread1.started.connect(self.worker1.threadJobPlayer1)
        self.thread1.start()

        self.thread2 = QThread()
        self.worker2 = Worker(None, None, None, None, self.Objects)
        self.worker2.moveToThread(self.thread2)
        self.thread2.started.connect(self.worker2.updateObjects)
        self.thread2.start()

    def initProcess(self):
        self.ex_pipe, self.in_pipe = mp.Pipe()

        self.jw = jobWorker(self.in_pipe)
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

            return


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    def __init__(self, pipe: Pipe, player: Car.Player, keysPressed, pipe1: Pipe, Objects):
        super().__init__()
        self.Objects = Objects
        self.pipe1 = pipe1
        self.pipe = pipe
        self.player = player
        self.keysPressed = keysPressed

    def threadJobPlayer(self):
        while True:
            self.player.game_update(self.pipe.recv())
            time.sleep(0.0167)

    def threadJobPlayer1(self):
        while True:
            self.player.game_update(self.pipe1.recv())
            time.sleep(0.0167)

    def updateObjects(self):
        while True:
            for b in self.Objects:
                b.game_update()
            time.sleep(0.0167)