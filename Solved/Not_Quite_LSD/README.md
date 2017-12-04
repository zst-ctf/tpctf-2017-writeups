# Not Quite LSD
Steganography - 30 points

## Challenge 
> Everybody loves LSD!

> Authors: Kevin Higgs, Chris Tong

[lsd.png](lsd.png)

## Hint
What did you think I meant?


## Solution

Upon seeing plane 0 in StegSolve, we see some white pixels at the upper left corner in all 3 (R, G, B).

LSD means least significant digit? Hence, the solution is LSB(red) + LSB(green) + LSB(blue)

	$ python3 solve.py 
	010101000101000001000011010101000100011001111011001100010111001101000010010111110110100100110101010111110100101100110000001100000110110001111101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

[Convert to ascii](https://www.rapidtables.com/convert/number/binary-to-ascii.html)

	TPCTF{1sB_i5_K00l}

## Flag
`TPCTF{1sB_i5_K00l}`