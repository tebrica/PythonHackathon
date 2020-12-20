import sys
import Car
import Object

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


class Scene(QGraphicsScene):
    def __init__(self, parent = None):
        QGraphicsScene.__init__(self, parent)

        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get 60Hz refresh (hopefully)
        self.timer = QBasicTimer()
        self.timer.start(FRAME_TIME_MS, self)

        bg = QGraphicsRectItem()
        bg.setRect(-1,-1,SCREEN_WIDTH+2,SCREEN_HEIGHT+2)

        self.player = Car.Player()
        self.player.setPos((SCREEN_WIDTH-self.player.pixmap().width())/2,
                           (SCREEN_HEIGHT-self.player.pixmap().height())/2)
        self.Objects = [Object.Object(PLAYER_Object_X_OFFSETS[0],PLAYER_Object_Y)]
        for b in self.Objects:
            b.setPos(SCREEN_WIDTH,SCREEN_HEIGHT)
            self.addItem(b)
        self.addItem(self.player)

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.show()
        self.view.setFixedSize(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.setSceneRect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = Scene()
    sys.exit(app.exec_())