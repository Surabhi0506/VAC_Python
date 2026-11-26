import threading

def greet(name):
    print("Hello", name)

t1 = threading.Thread(target=greet, args = ("Swara"))
t1.start()
t1.join()