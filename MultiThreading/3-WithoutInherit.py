from threading import Thread
import threading


class natural:
    def numbers(self):
        print(threading.current_thread().getName())
        for x in range(1, 11):
            print(x)


obj = natural()
t1 = Thread(target=obj.numbers)
t1.start()
