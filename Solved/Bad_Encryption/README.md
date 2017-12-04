# Bad Encryption
Reverse Engineering - 100 points

## Challenge 
> I was making an encryption program, but it is far from perfect. Instead of make the encryption work, I decided to just encrypt everything 100 times.

> Author: Kevin Higgs

[encode.py](encode.py) 

[encoded.zip](encoded.zip)

## Hint
> I bet the encryption works at least most of the time.


## Solution
After refactoring, [encode_modified.py](encode_modified.py), we see that the RGB pixels of the image are the `rand1`, `rand2` followed by `round( ch*(rand1/256)*(rand2/256) * 10)`.

Hence, we can make a script to check if the pixel values are valid. There will be a lot of possibilities, hence get the most common valid chars for each position.

	$ mkdir encoded
	$ cd encoded
	$ unzip ../encoded.zip
	$ cd ..
	$ python3 solve.py 

## Flag
`tpctf{i_c4nt_7h1nk_0f_a_fUnny_f14g_:(}`