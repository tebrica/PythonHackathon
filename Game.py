import sys
import threading
import Car
import Object
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFrame, QLabel, QWidget
from PyQt5.QtGui import QBrush, QImage, QPalette, QIcon, QPixmap
from PyQt5.QtCore import Qt
from multiprocessing import Queue, Process, Pipe
from player import Player
import time, random
import multiprocessing as mp
from JobWorker import jobWorker
from PyQt5.QtCore import (
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
        self.player = Car.Player(self, Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down, "player1.png", "player1_left.png",
                                 "player1_right.png", (SCREEN_WIDTH / 2) + 200, ((SCREEN_HEIGHT) - 250))
        self.player1 = Car.Player(self, Qt.Key_A, Qt.Key_D, Qt.Key_W, Qt.Key_S, "player2.png", "player2_left.png",
                                  "player2_right.png",(SCREEN_WIDTH / 2 )-200,((SCREEN_HEIGHT) - 250))

        self.Objects = [Object.ObjectCar1(self, 150, 580),
                        Object.ObjectCar2(self, 580, 900),
                        Object.ObjectCar3(self, 150, 580),
                        Object.ObjectCar4(self, 580, 900)]

        self.keys_pressed = set()
        self.setFocusPolicy(Qt.StrongFocus)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        ex_pipe, in_pipe = mp.Pipe()
        self.jw = jobWorker(in_pipe)
        self.t = threading.Thread(target=self.threadJob, args = (ex_pipe,))
        self.jw.start()
        self.t.start()




    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player1.game_update(self.keys_pressed)
        self.player.game_update(self.keys_pressed)
        for b in self.Objects:
            b.game_update()

    def threadJob(self, pipe1: Pipe):
        while True:
            value = pipe1.recv()
            print(value)
        #self.thread = QThread()
        #self.moveToThread(self.thread)
