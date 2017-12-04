# Super Encryption
Reverse Engineering - 60 points

## Challenge 
> My friend sent me a flag encrypted with an encryption program. Unfortunately, the decryption doesn't seem to work. Please help me decrypt this: `dufhyuc>bi{{f0|;vwh<~b5p5thjq6goj}`

> Author: Kevin Higgs

[superencrypt](superencrypt)

## Solution
Open this up in Hopper decompiler, we see the `encrypt()` function.

[Hopper psuedocode](encrypt.c) --> [My simplified version](encrypt-simplified.c)

So what I see is each char goes through a complex floating point thingy, afterwhich every 5 chars are reversed and then every 3 chars are reversed. I have implemented this as `flip_order_if_multiple(text, n)` in my python script

Next, I couldn't understand what the floating point stuff were in the code, hence I decided to manually find out the difference in characters between the input and output, done as `find_delta()`. Run through `update_offset()` to update a lookup table of delta offset values.

Finally, from the delta offset values, each char of the ciphertext will have the delta value subtracted.

It goes through flipping of 3 and 5 chars to retrieve the original flag!

	$ python3 test.py 
	...
	Decrypt: ctf_tpY4Y_r{f0r3rsg3v_3n3rein3gni}
	Flip: tpctf{Y4Y_f0r_r3v3rse_3ngin33ring}

## Flag
`tpctf{Y4Y_f0r_r3v3rse_3ngin33ring}`