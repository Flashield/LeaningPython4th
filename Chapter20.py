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