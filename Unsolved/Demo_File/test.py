#!/usr/bin/env python3
import re
with open('strings.txt', 'r') as f:
    text = f.read()

def filter(text):

    text = text.split('IEND', 1)[1]

    lines = text.split('. ')
    success = []
    for line in lines:
        if ('Just kidding' in line or
            'Of course, that isn\'t the flag' in line or
            'It\'s not true' in line):
            success.pop()

        if ('least favorite' in line or
            'doesn\'t like' in line or
            'isn\'t' in line or 
            'not' in line or 
            'fake' in line or 
            'Fun fact:' in line):
            pass
        else:
            if 'TPCTF{' in line:
                success.append(line)

    print(len(success))

    print('\n'.join(success))

    
def extract(text):
    found = re.findall(r'TPCTF\{.{18}\}', text)
    print('\n'.join(found))

extract(text)
