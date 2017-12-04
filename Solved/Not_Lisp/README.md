# Not Lisp
Misc - 20 points

## Challenge 
> ctong610 is trying to write a program, but he's really bad at programming so his program has both syntax errors and is way too long. If he has 10^4 pairs of parentheses, in how many ways can they be organized validly? (Note: (()()) is valid, but (()()( is not).

> Give your answer as a number mod 10^3.

> Note: ^ in this case is exponentiation, not xor.

> The flag is just a number.

> Author: Chris Tong

## Solution

Searching "lisp parentheses combinations" leads me to this [Stackoverflow page](https://stackoverflow.com/questions/727707/finding-all-combinations-of-well-formed-brackets).

There is an unanswered comment which says: 
> *Does anyone know why the number of well-formed 2n brackets is C(2n, n) - C(2n, n+1)*

---

Let's use [Wolfram Alpha to calculate it][1] for us: 
`C(2n, n) - C(2n, n+1) where n = 10^4`

We get a super long answer. Since the challenge asks for mod 1000, we can just look at the last 3 digits which happens to be `640`

*(PS. Never bruteforce ._.)*

## Flag
`640`

[1]: http://www.wolframalpha.com/input/?i=C(2n,+n)+-+C(2n,+n%2B1)+where+n+%3D+10%5E4