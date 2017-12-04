#!/usr/bin/env python3

offset = [-999 for i in range(40)]

def split_every(line, n):
    return [line[i:i+n] for i in range(0, len(line), n)]

def flip_order_if_multiple(line, multiple):
    splits = split_every(line, multiple)
    for i, each in enumerate(splits):
        if len(each) == multiple:
            splits[i] = each[::-1]
    return ''.join(splits)

def find_delta(orig, after):
    change = None
    for i, ch in enumerate(after):
        if orig[i] != ch:
            if not change:
                change = (i, ch)
            else:
                raise Exception('more than one offset change!?')
    return change

def update_offset(enc_orig, enc_after, in_orig, in_after):
    i, ch = find_delta(enc_orig, enc_after)

    in_after = flip_order_if_multiple(in_after, 5)
    in_after = flip_order_if_multiple(in_after, 3)
    i1, ch1 = find_delta(in_orig, in_after)

    # assert i == i1, f"the position differs! {i} , {i1}"

    delta = ord(ch) - ord(ch1)
    offset[i1] = delta

    print(f'Change at position {i1} with delta {delta}')


#################################################################
enc_base = 'BBAJFFKKJKJAAAKIEEBJIDCCCCDBDDABBA'
in_base = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDBDDABBB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDBDDBBBA', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDBDDACBA', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDBDDABCA', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCDDBDDABBA', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAA')

#################################################################
enc_base = 'BBAJFFKKJKJAAAKIEEBJIDCCCCDDDB'
in_base = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
#update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCDDDDB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAB')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCDCDDDB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAAABA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDEDB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAAABAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDDEB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAAABAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCDDDC', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAAABAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEECJIDCCCCDDDB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAAABAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCDCCDDDB', in_base, 'AAAAAAAAAAAAAAAAAAAAAAABAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDDCCCDDDB', in_base, 'AAAAAAAAAAAAAAAAAAAAAABAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIECCCCDDDB', in_base, 'AAAAAAAAAAAAAAAAAAAAABAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJIDCCCCEDDB', in_base, 'AAAAAAAAAAAAAAAAAAAABAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEFBJIDCCCCDDDB', in_base, 'AAAAAAAAAAAAAAAAAAABAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIFEBJIDCCCCDDDB', in_base, 'AAAAAAAAAAAAAAAAAABAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKJEEBJIDCCCCDDDB', in_base, 'AAAAAAAAAAAAAAAAABAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBJJDCCCCDDDB', in_base, 'AAAAAAAAAAAAAAAABAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBKIDCCCCDDDB', in_base, 'AAAAAAAAAAAAAAABAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAAKIEEBKIDCCCCDDDB', in_base, 'AAAAAAAAAAAAAABAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJLJAAAKIEEBJIDCCCCDDDB', in_base, 'AAAAAAAAAAAAABAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAAALIEEBJIDCCCCDDDB', in_base, 'AAAAAAAAAAAABAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJAABKIEEBJIDCCCCDDDB', in_base, 'AAAAAAAAAAABAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJABAKIEEBJIDCCCCDDDB', in_base, 'AAAAAAAAAABAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAKFFKKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'AAAAAAAAABAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKKKJAAAKIEEBJIDCCCCDDDB', in_base, 'AAAAAAAABAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKLJKJAAAKIEEBJIDCCCCDDDB', in_base, 'AAAAAAABAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFLKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'AAAAAABAAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJBAAKIEEBJIDCCCCDDDB', in_base, 'AAAAABAAAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBBJFFKKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'AAAABAAAAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BCAJFFKKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'AAABAAAAAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'CBAJFFKKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'AABAAAAAAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFGKKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'ABAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJGFKKJKJAAAKIEEBJIDCCCCDDDB', in_base, 'BAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')


cipher = 'dufhyuc>bi{{f0|;vwh<~b5p5thjq6goj}'
newcipher = ''
for i, ch in enumerate(cipher):
    ch = ord(ch)
    ch -= offset[i]
    newcipher += chr(ch)

print('Decrypt:', newcipher)

newcipher = flip_order_if_multiple(newcipher, 3)
newcipher = flip_order_if_multiple(newcipher, 5)
print('Flip:', newcipher)

'''
update_offset(enc_base, 'BBAJFFKKJKKAKAA', in_base, 'AAAAAAAAAAAAAAB')
update_offset(enc_base, 'BBAJFFKKJLJAKAA', in_base, 'AAAAAAAAAAAAABA')
update_offset(enc_base, 'BBAJFFKKJKJALAA', in_base, 'AAAAAAAAAAAABAA')
update_offset(enc_base, 'BBAJFFKKJKJAKBA', in_base, 'AAAAAAAAAAABAAA')
update_offset(enc_base, 'BBAJFFKKJKJAKAB', in_base, 'AAAAAAAAAABAAAA')
update_offset(enc_base, 'BBAKFFKKJKJAKAA', in_base, 'AAAAAAAAABAAAAA')
update_offset(enc_base, 'BBAJFFKKKKJAKAA', in_base, 'AAAAAAAABAAAAAA')
update_offset(enc_base, 'BBAJFFKLJKJAKAA', in_base, 'AAAAAAABAAAAAAA')
update_offset(enc_base, 'BBAJFFLKJKJAKAA', in_base, 'AAAAAABAAAAAAAA')
update_offset(enc_base, 'BBAJFFKKJKJBKAA', in_base, 'AAAAABAAAAAAAAA')
update_offset(enc_base, 'BBBJFFKKJKJAKAA', in_base, 'AAAABAAAAAAAAAA')
update_offset(enc_base, 'BCAJFFKKJKJAKAA', in_base, 'AAABAAAAAAAAAAA')
update_offset(enc_base, 'CBAJFFKKJKJAKAA', in_base, 'AABAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJFGKKJKJAKAA', in_base, 'ABAAAAAAAAAAAAA')
update_offset(enc_base, 'BBAJGFKKJKJAKAA', in_base, 'BAAAAAAAAAAAAAA')
print(offset)
'''
