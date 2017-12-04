# IRC
Web - 50 points

## Challenge 
> The bot flagbotbot on [#tpctf-chal](https://kiwiirc.com/client/irc.freenode.net/#tpctf-chal) has a flag, but has only a 3% chance of giving it out. The other 97% of the time, it gives out flegs. Flegs look like flags. Don't get fooled by flegs. You can get flagbotbot talking by waiting 30 seconds.

> Author: Clarence Lam

## Hint
> There isn't a good way to solve this other than staring at the chat box for a while. If you don't want to do that, get someone else to do it. Or something else, for that matter.


## Solution

The flagbot only posts every 30 sec. It will post fake "flegs" like this:

> @flagbotbot
the flag is TPCTF{ll11lI1|lI11} that's a fleg btw 

---

Wait until the flagbot returns the real flag

> @flagbotbot
the flag is TPCTF{1lI|1Il|1I1l} that's a flag btw 

I was lucky to have it appear a few min after I logged in. Otherwise, keep it open / log it to a local file and check back later,

## Flag
`TPCTF{1lI|1Il|1I1l}`