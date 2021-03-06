import re

hand = open('regex_sum_1166787.txt')
sum = 0;

for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    for num in stuff:
        sum +=int(num)

print(sum)