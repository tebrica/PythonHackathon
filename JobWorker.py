from multiprocessing import Process, Pipe
import time

class jobWorker(Process):

    def __init__(self, pipe1: Pipe):
        super().__init__(target=self.function, args=(pipe1,))

    def function(self, pipe1: Pipe):
        while True:
            pipe1.send("Go")
            time.sleep(0.5)