from threading import Thread
import threading


class Natural(Thread):
    def run(self):
        print(threading.current_thread().getName())
        for x in range(1, 11):
            print(x)


obj = Natural()
obj.run()  # run inside the main thread

obj.start()  # run in new thread
