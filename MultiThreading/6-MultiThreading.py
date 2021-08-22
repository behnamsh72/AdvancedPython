from threading import Thread
import threading


def nature_Number():
    print(threading.current_thread().getName()," Has been started\n\n")

    for x in range(1, 11):

        print(x)

    print(threading.current_thread().getName()," Has been Ended\n\n")

t1 = Thread(target=nature_Number)
t2 = Thread(target=nature_Number)
t1.start()
t2.start()
