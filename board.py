from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFrame, QLabel, QWidget
from PyQt5.QtGui import QBrush, QImage, QPalette, QIcon, QPixmap
from PyQt5.QtCore import Qt
from multiprocessing import Queue, Process
from player import Player

class Game(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.board = Board(self)
        self.setCentralWidget(self.board)

        self.resize(1200, 850)
        self.center()
        self.setWindowTitle('Crazy Cars')
        self.setWindowIcon(QIcon("Slike/cc.jpg"))

        # setting background picture
        oImage = QImage("Slike/bck.jpg")
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


class Board(QFrame):

    BoardWidth = 1200
    BoardHeight = 850

    def __init__(self, parent):
        super().__init__(parent)

        self.init_board()

    def init_board(self):
        self.q = Queue()

        #dva igraca
        self.player1 = Player(self, 815, 650, "Slike/player1.png")
        self.player2 = Player(self, 270, 650, "Slike/player2.png")

        self.keys_pressed = set()

        self.startProcess()

        self.setFocusPolicy(Qt.StrongFocus)

    def startProcess(self):
        self.p = Process()
        self.p.start()

    #da li je pritisnut taster

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

        if Qt.Key_Left in self.keys_pressed:
            self.move_player(self.player1, self.player1.x - 10, "Slike/player1_left.png")
        if Qt.Key_Right in self.keys_pressed:
            self.move_player(self.player1, self.player1.x + 10, "Slike/player1_right.png")
        if Qt.Key_A in self.keys_pressed:
            self.move_player(self.player2, self.player2.x - 10, "Slike/player2_left.png")
        if Qt.Key_D in self.keys_pressed:
            self.move_player(self.player2, self.player2.x + 10, "Slike/player2_right.png")

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

        key = event.key()

        if key == Qt.Key_Left:
            self.changePicture(self.player1, "Slike/player1.png")
        if key == Qt.Key_Right:
            self.changePicture(self.player1, "Slike/player1.png")
        if key == Qt.Key_A:
            self.changePicture(self.player2, "Slike/player2.png")
        if key == Qt.Key_D:
            self.changePicture(self.player2, "Slike/player2.png")

    def changePicture(self, label, newPicture):
        picture = QPixmap(newPicture)
        picture = picture.scaled(120, 160)
        label.setPixmap(picture)

    def move_player(self, player, newX, newPicture):

        if newX < Board.BoardWidth-330 and newX > 220:
            self.player = player
            self.changePicture(self.player, newPicture)
            self.player.x = newX
            self.player.move(newX, self.player.y)
            self.show()

    def timerEvent(self, event):
        self.update()