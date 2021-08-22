import threading

for x in range(1, 11):
    print(x)

print(threading.currentThread().getName())

