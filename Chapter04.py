S="Hel\nlo\tWo\rld!"
print(S)
print(S.isalpha())
print(S.isprintable())
line='Hello, W,orl,d'
print(line.split(",",2))
print(dir(S.replace('d','k')))
print({x:ord(x) for x in 'spaam'})
T=(1,2,3,4,2,2)
print(T.count(2))
f=open('Hello.txt','w')
f.write("Hello,World!\n")
f.write("Test,File!")
f.close()
import fractions
f=fractions.Fraction(2,3)
print(f+fractions.Fraction(7,5))
X=None
print([X]*2)
print(type(X))
print(isinstance([X], list))