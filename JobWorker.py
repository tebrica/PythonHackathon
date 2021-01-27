from multiprocessing import Process, Pipe
import time

from PyQt5.QtWidgets import QFrame


class jobWorker(Process):

    def __init__(self, pipe1: Pipe, pipeHS: Pipe, pipeHS1: Pipe):
        super().__init__(target=self.function, args=())
        self.keys_pressed = set()
        self.pipe = pipe1
        self.pipeHS = pipeHS
        self.pipeHS1 = pipeHS1
        self.brojac = 0
        self.carBod = 0
        self.car1Bod = 0
        self.carCoin = False
        self.car1Coin = False

    def function(self):
        while True:
            self.pipe.send("go")
            time.sleep(0.016)

            if self.carCoin:
                self.carBod = self.carBod + 100
                self.pipeHS.send(str(self.carBod))


            if self.car1Coin:
                self.car1Bod = self.car1Bod + 100
                self.pipeHS1.send(str(self.car1Bod))

            if self.brojac == 60:
                self.carBod = self.carBod +10
                self.car1Bod = self.car1Bod + 10

                self.pipeHS.send(str(self.carBod))
                self.pipeHS1.send(str(self.car1Bod))

                self.brojac = 0

            self.brojac = self.brojac + 1

    def coinCar(self):
        self.carCoin = True

    def coinCar1(self):
        self.car1Coin = True

    def stop(self):
        self.pipe.send("stop")
        self.kill()