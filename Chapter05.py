print(repr(1/3))
print(str(1/3))
print(1==2<3) #1==2 & 2<3
print((1==2)<3)
print(1==(2<3)) 
print(5/3)
print(5//3) #真除法，去除小数部分
print(5//3.0)
print(2**1024)
print(int(64),int('25',8),0o25,int('25',16),0x25,int('25',13)) #还能转换成其他的进制，有意思。
print('{0:o},{2:x},{1:b}'.format(25,24,23))
print('{0:o},{1:x},{2:b}'.format(25,24,23))
print(0.1+0.1+0.1-0.3)
from decimal import Decimal
import decimal
decimal.getcontext().prec = 4
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))
print(Decimal(0.1)+Decimal(0.1)+Decimal(0.1)-Decimal(0.3))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(repr(decimal.Decimal('1.00') / decimal.Decimal('3.00')))
    
from fractions import Fraction
print(Fraction('.44') + Fraction('1.25'))
print(Fraction(*(2.5).as_integer_ratio()))
print(Fraction(1000, 1234567890))
print(Fraction(*(4/3).as_integer_ratio()))
print(Fraction(*(4/3).as_integer_ratio()).limit_denominator(10))
a=Fraction(*(4/3).as_integer_ratio())
print(a.limit_denominator(10))
x=set("abcd")
y=set("cdef")
print(x)
print(x|y)
print(x.update({'d','f','g'}))
print(x)
print(True+5)