import threading
import time

def greet1():
    time.sleep(2)
    print("Helloooooooooooooooooooooooooooooo")

def greet2():
    time.sleep(1)
    print("Helloooooooooooooooo bhondussssss")

def greet3():
    print("Helloooooooooooooooo bhondussssss")


t1 = threading.Thread(target=greet1)
t2 = threading.Thread(target=greet2)
t3 = threading.Thread(target=greet3)

t1.start()
t1.join()
t2.start()
t3.start()
print("Main program continues")