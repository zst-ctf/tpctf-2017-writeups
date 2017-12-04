# Zalgo
Slightly More Trivial - 2 points

## Challenge 
> t̤̬̫͖̬̊ͪ̏ͤ̈́ͬ͆͌̃̉̀̊̽͌ͯ͑͋̍́̀̚͝p̸͒̓ͨ̐̒ͬ̿̇̄̋̓̌͋͂͟͡҉̡̞̝̳͇͉̥͔͖̣̭͕̫͖͓̱̟̲c̥͕̭̬̹̯̳̮̳̻̬͇̖̜͇̺̝ͦͤ́͋̕͡tͦ́̊̑͊͋̎ͨ͒̋͆́́̓ͥ̋͡҉̥̲̟̰̬̦̰͘f̷̡̜̙̣̙̮͕͒̊͊̏ͧͩͦ̿͑ͦ̏̀́͡{̴̛̔̈͆̆͋̂͗̇̀͏͙̺͈͕̝͕̗h̡̺̞͉̤̠̥͆̔͋ͬͪ͂̕͟͞é͚̻͔̝ͨ̽́ͬ̀̿̆ͤͪͣ̍ͦ́̌ͩ͢͠͠͠ͅ_̸̵̡͖͉͕̫̩̱͈̻̥̮̭̖͓̞͕̲̱̆̏ͧ̽̏ͩ̅ͣ̈̈́̾̈́̓ͯ̀͟cͦͮͮ̽̇̓̾̏͏̨̠͎͙̖̲̫̲̳̣ơ̭̗̲̭̜̗̲̤̰̗̝̗̩̹̗̤͖̝ͦͣ͆ͦ̌̒̃̽̋ͣ͑̀͡m̢̧͔͕̙̬̦̲̘̙͓̟̥̮̭ͣ͐ͮ̇͘͝e̸͇̞͔̱̞̱̘͖͓̠̥̲͚͇̦̤̜̍ͭ͒͊ͧ͑̇́̊̾́͆̊͗̏̈́͗͡s̓ͪ̂ͨ̔̂͌͏̶̴̨̱͙͇̝̖͙͉͎̜͈̱̻͘}̨̡̻̺͍͔͍̰̫̫̹̬ͥͭͥͨ̌
> Author: Clarence Lam

## Hint
> I really don't think you need a hint for this one.

## Solution
The flag is hidden within Unicode diacritics of some sort?

Filter out printable characters to retrieve the flag

	$ python3
	
	>>> with open("garbled.txt", "r") as f:
	...     text = f.read()

	>>> import string
	>>> ''.join(list(filter(lambda x: x in string.printable, text)))
	'tpctf{he_comes}'

## Flag
`tpctf{he_comes}`