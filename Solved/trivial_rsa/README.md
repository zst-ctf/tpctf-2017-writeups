# trivial rsa
Slightly More Trivial - 3 points

## Challenge 
> n=65561
e=65537
c=27830
m^e=c (mod n)
m=?

> Flag format is tpctf{m}

> Author: Clarence Lam

## Solution

From factordb.com:

	65561 = 53 · 1237

Putting into a script:
	
	$ python3 solve.py 
	tpctf{31337}

## Flag
`tpctf{31337}`