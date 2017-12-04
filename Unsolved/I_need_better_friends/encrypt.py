from decimal import *
from binascii import hexlify as h
from binascii import unhexlify as u
from math import ceil as e
from sys import argv as y
D,w,O,z,j,b,X,v,o,U=Decimal,getcontext,chr,len,str,int,long,str,len,hex
def q():
    w().prec+=5;L,t,s,n,k,d,K=0,D(3),3,1,0,0,24
    while s!=L:L=s;n,k=n+k,k+8;d,K=d+K,K+32;t=(t*n)/d;s+=t
    w().prec-=5
    return +s
Q=q()
def s(x):
    w().prec+=5;i,L,s,f,n,S=1,0,x,1,x,1;
    while s!=L:L=s;i+=2;f*=i*(i-1);n*=x*x;S*=-1;s+=n/f*S
    w().prec-=5
    return +s
def E(S):
    w().prec=b(e(o(S)*2.40823996531))+1;a=(lambda:[D(O(48)+O(46)+j((lambda:X(h(S),4+4*4-4))()))*Q-Q/D(2),j(v(D(5.2))+S)+v(U(z(j(e(2.71)))))][0])()
    return j((lambda P:U(X(v((D(1)-s(a)*s(a+D(1)-D(7-5)+D(3)-D(6-4))).sqrt())[2:])))(lambda:[-2,X(j(v(1)),13)][1]))[2:-1]
A=h("Usage: "+y[0]+" <string>") if o(y)!=2 else E(y[1])
f=open("out.txt",O(b('7'+'7',(4**4)/4/4)))
f.write(u(A[:-1] if z(A)%2==1 else A))
f.close()