def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5]))

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5,6]))

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5,6,7]))
print(mysum(['spam', 'ham', 'eggs']))

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)

print(mysum([1, 2, 3, 4, 5,6,7,8]))
print(mysum(['spam', 'ham', 'eggs']))

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
L = [1, [2, [3, 4], 5], 6, [7, 8],9]
print(sumtree(L))

def sumtree2(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot

print(sumtree2(L))

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c
print(func(1,2,3))
print(func.__annotations__)

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))

x = (lambda a="fee", b="fie", c="foe": a + b + c)
print(x("wee"))

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action
act1=knights()
print(act1("Robin"),act1)

key = 'got'
print({'already': (lambda: 2 + 2),
'got':(lambda: 2 ** 4),
'one':(lambda: 2 ** 6)}[key]())

lower = (lambda x, y: x if x < y else y)
print(lower('aa','13'))

import sys
showall = lambda x: list(map(sys.stdout.write, x))
showall(['spam\n', 'toast\n', 'eggs\n'])

def action(x):
    return (lambda y: x + y)
act = action(99)
print(act)
print(act(2))

action = (lambda x: (lambda y: x + y))
act = action(99)
print(action(99))
print(act(3))
print(((lambda x: (lambda y: x + y))(99))(4))


import operator, functools
print(functools.reduce(operator.add, [2, 4, 6]))
print(functools.reduce((lambda x, y: x + y), [2, 4, 8]))

