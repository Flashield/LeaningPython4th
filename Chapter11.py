a,b,c,d = "Spam"
print(a,b,c,d,a+b+c+d)
i,*j="Hello"
print(i,j)
print(range(3),list(range(3)))
import sys
temp=sys.stdout
print(temp)
sys.stdout=open("Chapter11.log","a")
print("Hello,World!Chapter11")
sys.stdout.close()
sys.stdout = temp
print("Back to ?")
print(open("Chapter11.log").read())