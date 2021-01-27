from multiprocessing import Process, Pipe
import time

from PyQt5.QtWidgets import QFrame


class jobWorker(Process):

    def __init__(self, pipe1: Pipe):
        super().__init__(target=self.function, args=())
        self.keys_pressed = set()
        self.pipe = pipe1

    def function(self):
        while True:
            self.pipe.send("go")
            time.sleep(0.016)

    def stop(self):
        self.pipe.send("stop")
        self.kill()