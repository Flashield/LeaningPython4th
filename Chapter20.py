print(list(map(ord, 'spamq')))
print([x ** 2 ** 2 for x in range(10)])
print(list(map((lambda x: x ** 2), range(10))))
print([x ** 2 for x in range(10) if x % 2 == 0])
print('5:',list( map((lambda x: x**2), filter((lambda x: x % 2 == 1), range(10))) ))
print([x + y for x in [0, 1, 2, 3] for y in [100, 200, 300, 400]])
print([(x, y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 == 1])

M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
print([row[1] for row in M])
print([M[row][2] for row in (0, 1)])
print([[col + 10 for col in row] for row in M])
print(open('Hello.txt').readlines())
print([line.rstrip() for line in open('Hello.txt').readlines()])
print([line.rstrip() for line in open('Hello.txt')])
print(list(map((lambda line: line.rstrip()+'3'), open('Hello.txt').readlines())))
listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]
print([age for (name, age, job) in listoftuple])
print(list(map((lambda row:row[1]),listoftuple)))

def gensquares(N):
    for i in range(N):
        yield (i+1) ** 2
x=gensquares(4)
print(x)
print(next(x))
print(next(x))
print(next(x))

def gen():
    for i in range(10):
        X = yield i+1
        print(X)
G=gen()
print(next(G))
#print(G.send(10))
#print(G.send(20))
print(next(G))
'''注释'''
print((x ** 2 for x in range(4)))
print(list(x ** 2 for x in range(4)),tuple(x ** 2 for x in range(4)))
print(''.join(x for x in 'aaa,bbb,ccc'.split(',')))
print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))

line = 'aa bbb c'
print(''.join(x for x in line.split() if len(x) > 1))
print(list(map(lambda x:x , line.split())))
print(''.join(map(lambda x:x.upper() ,line.split())))

G = (c * 4 for c in 'SPAM')
print(iter(G) is G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))

def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i
B=both(5)
print(next(B))
print(list(B))

import os
for (root, subs, files) in os.walk(r'.'):
    for name in files:
        print(root,subs, name)

D = dict(a='Bob', b='dev', c=40.5)
def f(a, b, c): print('%s, %s, and %s' % (a, b, c))
print(f(*D))

L, S = [1, 2, 3], 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

print(list(map(lambda x, y: x + y, open('Chapter04.py'), open('Chapter05.py'))))
