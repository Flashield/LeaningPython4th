L=[1,2,3]
b=L
b[1]="Hello"
print(L)

def multiple(x, y): #虽说没有类型，但是类型无处不在
    x = 2
    y = [3, 4]
    return x, y
X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X,L)

def f(a,b,c):
    return a,b,c
print(f(1,2,3))
print(f(1,b=3,c=2))

def f(*arg):
    print(arg)
f("heloo",1,"Go")

def f2(**arg):
    print(arg)
#f2("heloo",1,"Go")#抛出异常
f2(a=1,b=2,c="Go")

def f(a, *pargs, **kargs): print(a, pargs, kargs)
f(1, 2, 3, x=1, y=2,c="k")

def func(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func(*args)

args = {'a': 1, 'b': 6, 'c': 3}
args['d'] = 4
func(**args)

func(*(1, 2), **{'d': 4, 'c': 9})

def tracer(func, *pargs, **kargs):
    print('calling:', func.__name__)
    return func(*pargs, **kargs)

def func(a, b, c, d):
    print(a,b,c,d)
    return a + b + c + d

print(tracer(func, 1, 2, c=6, d=4))

def kwonly(a, *b, c):print(a, b, c)
kwonly(1, 2, c=3)
try:
    kwonly(1, 2, 3)
except Exception as ex:
    print(ex)
    
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))#人类太聪明了
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res: continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

print(intersect("helle","gooeldbye","anythinlge"))
print(union("hello","goodbye","anything"))