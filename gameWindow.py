import sys
import Car
import Object
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFrame, QLabel, QWidget
from PyQt5.QtGui import QBrush, QImage, QPalette, QIcon, QPixmap
from PyQt5.QtCore import Qt
from multiprocessing import Queue, Process
from Car import Player
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

SCREEN_WIDTH            = 1200
SCREEN_HEIGHT           = 850
PLAYER_SPEED            = 3   # pix/frame
PLAYER_Object_X_OFFSETS = [0,45]
PLAYER_Object_Y         = 15
Object_SPEED            = 10  # pix/frame
Object_FRAMES           = 50
FRAME_TIME_MS           = 16  # ms/frame


class Scene(QGraphicsScene, QFrame):

    BoardWidth = 1200
    BoardHeight = 850

    def __init__(self, parent = None):
        super().__init__(parent)

        self.player = Car.Player(Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down, "player1.png", "player1_left.png",
                                 "player1_right.png")
        self.player1 = Car.Player(Qt.Key_A, Qt.Key_D, Qt.Key_W, Qt.Key_S, "player2.png", "player2_left.png",
                                  "player2_right.png")
        self.keys_pressed = set()

        QGraphicsScene.__init__(self, parent)

        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1, -1, SCREEN_WIDTH + 2, SCREEN_HEIGHT + 2)

        self.player.setPos((SCREEN_WIDTH - self.player.pixmap().width()) / 4+ (SCREEN_WIDTH) / 3,
                           (SCREEN_HEIGHT) - 250)

        self.player1.setPos((SCREEN_WIDTH - self.player.pixmap().width()) / 4 ,
                            (SCREEN_HEIGHT) - 250)

        self.Objects = [Object.Object(), Object.Object(), Object.Object(), Object.ObjectCar(), Object.ObjectCar()]
        for b in self.Objects:
            b.setPos(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.addItem(b)
        self.addItem(self.player)
        self.addItem(self.player1)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.setSceneRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()

    def game_update(self):
        self.player.game_update(self.keys_pressed)
        for b in self.Objects:
            b.game_update()
        self.player1.game_update(self.keys_pressed)
        for b in self.Objects:
            b.game_update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())