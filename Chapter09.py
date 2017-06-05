print((40),(40,))
from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])
print(bob,bob[1],bob.name)
import random
f=open("Hello.txt","a")
f.write("Hello,World!"+str(random.randint(0,100))+"\n")
f.close()
f=open("Hello.txt","rb+")
print(f.read())
f.close()
D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()
F = open('datafile.pkl', 'rb')
E=pickle.load(F)
print(E)
F.close()
import struct
print(struct.pack('>i4sh', 7, b'spam', 8))
print(struct.pack('>i2sh', 7, b'spam', 8))
help(struct)

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec,type(rec))
import json
print(json.dumps(rec),type(json.dumps(rec)))
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt', 'r').read())

a=[1,2,3,4]
while a :
    print(a)
    a.pop()

L=[1,2,3,4]
K1=["a",L,"b"]
K2=["a",L[:],"b"]
L[1]=0
print(K1,K2)