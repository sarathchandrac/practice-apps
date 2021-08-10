import threading

def hello_world():
    print("hello world")

def function1():
    for x in range(10):
        print('One')

def function2():
    for x in range(10):
        print('Two')

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t2.start()
t2.join()
t1.start()

