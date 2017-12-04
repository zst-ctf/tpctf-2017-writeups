from decimal import *
from binascii import hexlify as h
from binascii import unhexlify as u
from math import ceil as e
from sys import argv as y

O = chr
z = len

j = str

b = int

v = str
o = len
U = hex

Q=Decimal('3.141592653589793238462643383')

def s(x):
    getcontext().prec+=5;
    i,L,s,f,n,S=1,0,x,1,x,1;
    while s!=L:
        L=s;
        i+=2;
        f*=i*(i-1);
        n*=x*x;
        S*=-1;
        s+=n/f*S
    getcontext().prec-=5
    return +s

def E(S):
    getcontext().prec=b(e(o(S)*2.40823996531))+1;
    a=(lambda:[Decimal(O(48)+O(46)+j((lambda:long(h(S),4+4*4-4))()))*Q-Q/Decimal(2),j(v(Decimal(5.2))+S)+v(U(z(j(e(2.71)))))][0])()
    return j((lambda P:U(long(v((Decimal(1)-s(a)*s(a+Decimal(1)-Decimal(7-5)+Decimal(3)-Decimal(6-4))).sqrt())[2:])))(lambda:[-2,long(j(v(1)),13)][1]))[2:-1]
A=h("Usage: "+y[0]+" <string>") if o(y)!=2 else E(y[1])

f=open("out.txt", 'w')
f.write(u(A[:-1] if z(A)%2==1 else A))
f.close()