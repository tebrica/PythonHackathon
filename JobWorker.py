import threading
from multiprocessing import Process, Pipe
import time

from PyQt5.QtWidgets import QFrame

class jobWorker(Process):

    def __init__(self, pipe1: Pipe, pipeHS: Pipe, pipeHS1: Pipe):
        super().__init__(target=self.function, args=())

        self.pipe = pipe1
        self.pipeHS = pipeHS
        self.pipeHS1 = pipeHS1

        self.brojac = 0
        self.carBod = 0
        self.car1Bod = 0


    def function(self):
        while True:
            self.pipe.send("go")

            if self.brojac == 120:
                self.carBod = self.carBod + 10

            if self.brojac == 120:
                self.car1Bod = self.car1Bod + 10

                self.pipeHS.send(str(self.carBod))
                self.pipeHS1.send(str(self.car1Bod))

                self.brojac = 0

            self.brojac = self.brojac + 1

            time.sleep(0.008)

    def stop(self):
        self.pipe.send("stop")
        self.kill()