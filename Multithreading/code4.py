import threading

counter = 0

def increase_counter():
    global counter
    for _ in range(100000):
        00