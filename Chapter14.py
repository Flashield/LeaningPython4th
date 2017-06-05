f = open('Hello.txt')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

I=iter(f)
print(I.__next__())
print(I.__next__())

for line in f:
    print(line.lower(),end="")
f.close()

print([x+10 for x in list(range(5))])
f = open("testjson.txt")
lines=f.readlines()
print(lines)
f.close()

lines = [line.rstrip() for line in open("testjson.txt") if 's' in line.lower()]
print(lines)

print([x+y for x in 'abc' for y in 'hij'])
