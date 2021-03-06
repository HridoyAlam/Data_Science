import re
hand = open('short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >=0:
        print(line)

#using re.search()

hand = open('short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)