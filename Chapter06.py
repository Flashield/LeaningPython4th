L1=[2,3,4]
L2=L1
L3=L1[:]
print(L1==L2)
print(L1==L3)
print(L1 is L2)
print(L1 is L3)
L1[0]=5
print(L1)
print(L2)
print(L3)
print(L1==L2)
print(L1==L3)
print(L1 is L2)
print(L1 is L3)
import sys
print(sys.getrefcount("a"))