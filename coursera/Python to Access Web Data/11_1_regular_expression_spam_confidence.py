import re

hand =open('short.txt')
numlist = list()

for line in hand:
    line =line.rstrip()

    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print(f'Maximum:{max(numlist)}')

x= 'We just received $10.00 for choice.'
y = re.findall('\$[0-9.]+',x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

