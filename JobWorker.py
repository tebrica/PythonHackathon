from multiprocessing import Process, Pipe
import time

from PyQt5.QtWidgets import QFrame


class jobWorker(Process):

    def __init__(self, pipe1: Pipe, pipe2: Pipe, pipe3: Pipe):
        super().__init__(target=self.function, args=())
        self.keys_pressed = set()
        self.pipe = pipe1
        self.pipe2 = pipe2
        self.pipe3 = pipe3

    def function(self):
        while True:
            recv = self.pipe2.recv()
            self.pipe.send(recv)
            self.pipe3.send(recv)