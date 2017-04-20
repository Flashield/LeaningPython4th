print(str([1, 2]) + "34")
print([1,2]+list("34"))
L=['abc','ghj','Fde','Cik']
for x in L:
    print(x, end=",")
print("")
print(list(map(ord, 'spam')))
L.sort(key=None, reverse=False)
print(L)
L.sort(key=str.upper, reverse=False)
L.pop(1)
print(L)
L.remove('abc')
print(L)
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(D['ham'])
print('eggs' in D)
print(D.keys(),D.values(),list(D),list(D.items()))
for k in D:
    print("|{1:10} | {0:>10} |".format(k,D[k]))
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
print(dict(zip(['a', 'b', 'c'], [1, 2, 3])))