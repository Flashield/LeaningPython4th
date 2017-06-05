import os
print(os.path.getsize("Hello.txt"))

X = 99
def f1():
    X = 88
    def f2():
        print(X)
    f2()
f1()

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F=tester(0)
F('Hello')
F('Bye')

def func():
    x='Ni'
    def nested():
        nonlocal x
        x='Spam'
    nested()
    print(x)

func()