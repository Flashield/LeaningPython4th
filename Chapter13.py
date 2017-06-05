x = 10
while x:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=',')

print()
x = 10
while x:
    x = x - 1
    if x % 2 == 0:
        print(x, end=';')

y=121
x=[2,3,5,7,11]
for i in x:
    if y % i ==0:
        print("has factor {0}".format(i))
        break
    #i+=1
else:
    print("is prime")


x=[2]
y=3
while y<=10000:
    #y=x//2
    for z in x:
        if y % z == 0:
            print("{0} has factor {1}".format(y,z))
            break
    else:
        print("{0} is prime".format(y))
        x.append(y)
    y+=2
print(x)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])
    
for (key, value) in D.items():
    print(key, '=>', value)