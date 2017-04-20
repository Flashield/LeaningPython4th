print("Hello,\" World",'''Hell\o, \\'World!''')
path = r'C:\new\text.dat'
print(path,repr(path))
#''' #通过triple'进行整段程序的注释
print("Hello, World!")
print("Second Line!")
#'''
print("-"*20+"Seperate Line"+"-"*20)
s="1234567890"
print(s[2:4],s[-4:-2],s[-2:4],s[2:-2:2],s[::-1]) #Third number is step
print(str("string"),repr(repr(repr("string"))))
print(ord("2"),chr(114))

B = '1101' # Convert binary digits to integer with ord
I = 0
while B != '':
    I = I * 8 + (ord(B[0]) - ord('0'))
    B = B[1:]
    print(I)
print(int("1101",8),(0o1101))

print('That is %d %s bird!' % (1, 'dead'))
print('That is {0} {1} bird!'.format(1, 'dead'))
print("Hello,World".upper().capitalize())

s="abcdefgh"
L=list(s)
L[3]="5"
K="^".join(L)
print(K)
print("".join(K.split(sep="^")))
print('%f, %*.*f' % (1/3.0,2, 4,1/3.0))
print('%(qty)d more %(food)s' % {'qty': 2, 'food': 'spam'})
food = 'spam'
qty = 10
print(vars())
print('%(qty)d more %(food)s' % vars())
template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))
import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))
somelist = list('SPAM')
parts = (somelist[0], somelist[-1], somelist[1:3])
print(type(parts),'first={0}, last={1}, middle={2}'.format(*parts))
print('{0:10} = {1:10}'.format('spam', 123.4567))