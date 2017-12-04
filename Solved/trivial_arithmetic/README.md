# trivial arithmetic
Slightly More Trivial - 4 points

## Challenge 
> 0.1+0.2 == ?

Flag format is tpctf{answer}

Author: Clarence Lam

## Hint
> What's the f--ing point?


## Solution

Straight-forward if you follow /r/ProgrammerHumor bashing on adding floating-points

Some reference: [#1](https://www.reddit.com/r/javascript/comments/2scikz/eli5_why_is_this_true_01_02_030000000000000004/), [#2](https://www.reddit.com/r/ProgrammerHumor/comments/74y1i3/2_3_4999999999/)

	// In javascript console
	0.1 + 0.2
	>> 0.30000000000000004


## Flag
`tpctf{0.30000000000000004}`