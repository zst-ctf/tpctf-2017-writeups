# 768
Crypto - 30 points

## Challenge 
> oh no it's rsa

[768.txt](768.txt)

## Hint
Something seems funny about that modulus.

## Solution
From the hint, it means it is RSA-768.

A quick google search tells me it has been factored in 2009.
https://en.wikipedia.org/wiki/RSA_numbers#RSA-768

	RSA-768 = 12301866845301177551304949583849627207728535695953347921973224521517264005
	          07263657518745202199786469389956474942774063845925192557326303453731548268
	          50791702612214291346167042921431160222124047927473779408066535141959745985
	          6902143413
	RSA-768 = 33478071698956898786044169848212690817704794983713768568912431388982883793
	          878002287614711652531743087737814467999489
	        × 36746043666799590428244633799627952632279158164343087642676032283815739666
	          511279233373417143396810270092798736308917

If we look at `n` in the given [`768.txt`](768.txt) file, we realise that `n` is the exact same number but written in hex.
Hence, we have `p` and `q` from above!

---

Quick scripting

	$ python3 solve.py 
	It appears that you have managed to solve the challenge.
	Flag is tpctf{omg_b1c_m0dulus}.


## Flag
`tpctf{omg_b1c_m0dulus}`