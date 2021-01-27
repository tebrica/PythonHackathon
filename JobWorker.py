import threading
from multiprocessing import Process, Pipe
import time

from PyQt5.QtWidgets import QFrame


class jobWorker(Process):

    def __init__(self, pipe1: Pipe, pipeHS: Pipe, pipeHS1: Pipe, pipeCoin: Pipe):
        super().__init__(target=self.function, args=())

        self.pipe = pipe1
        self.pipeHS = pipeHS
        self.pipeHS1 = pipeHS1
        self.pipeCoin = pipeCoin

        self.brojac = 0
        self.carBod = 0
        self.car1Bod = 0

        self.carCoin = False
        self.car1Coin = False


    def function(self):
        while True:

            self.pipe.send("go")
            self.coin = self.pipeCoin.recv()

            if self.coin == "car":
                self.carCoin = True
            if self.coin == "car1":
                self.car1Coin = True

            if self.carCoin:
                self.carBod = self.carBod + 100 + 10
                self.pipeHS.send(str(self.carBod))

            if self.car1Coin:
                self.car1Bod = self.car1Bod + 100 + 10
                self.pipeHS1.send(str(self.car1Bod))

            if self.brojac == 60 and not self.carCoin:
                self.carBod = self.carBod + 10

            if self.brojac == 60 and not self.car1Coin:
                self.car1Bod = self.car1Bod + 10

                self.pipeHS.send(str(self.carBod))
                self.pipeHS1.send(str(self.car1Bod))

                self.brojac = 0

            self.brojac = self.brojac + 1
            self.carCoin = False
            self.car1Coin = False

            time.sleep(0.016)




    def stop(self):
        self.pipe.send("stop")
        self.kill()