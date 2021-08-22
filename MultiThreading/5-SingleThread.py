from threading import Thread
import threading


def multiply(a, b):
    print(threading.current_thread().getName())

    print("Multiplication result:", a * b)


def division(a, b):
    print(threading.current_thread().getName())

    print("Division Result:", a / b)


def targetFunction(a, b):
    multiply(a, b)
    division(a, b)


t1 = Thread(target=targetFunction, args=(10, 5))
t1.start()
