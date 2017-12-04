#!/usr/bin/env python3

# https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
# Took from SO
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

n = 65561
e = 65537
c = 27830
p = 53
q = 1237
phi = (p - 1) * (q - 1)
d = modinv(e, phi)

m = c**d % n

print(f"tpctf{{{m}}}")
