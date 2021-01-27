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

        #self.t = threading.Thread(target=self.coinThread, args=())

    def function(self):
        while True:

            self.pipe.send("go")

            if self.carCoin:
                self.carBod = self.carBod + 100
                self.pipeHS.send(str(self.carBod))
                self.carCoin = False

            if self.car1Coin:
                self.car1Bod = self.car1Bod + 100
                self.pipeHS1.send(str(self.car1Bod))
                self.car1Coin = False

            if self.brojac == 60:
                self.carBod = self.carBod + 10
                self.car1Bod = self.car1Bod + 10

                self.pipeHS.send(str(self.carBod))
                self.pipeHS1.send(str(self.car1Bod))

                self.brojac = 0

            self.brojac = self.brojac + 1

            #self.coin = self.pipeCoin.recv()
            #self.coin = "car"
            #if self.coin == "car":
               # self.carCoin = True
            #if self.coin == "car1":
               # self.car1Coin = True

            time.sleep(0.016)


    def coinThread(self):
        while True:

            time.sleep(0.1)

    def stop(self):
        self.pipe.send("stop")
        self.kill()