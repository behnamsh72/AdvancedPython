from threading import Thread


def swap_number(a, b):
    print("The thread has been started ")

    print("Numbers before swaping are ", a, " and ", b)
    temp = a
    a = b
    b = temp
    print("Numbers after swaping are ", a, " and ", b)


t1 = Thread(target=swap_number, args=(5, 6))
t1.start()
