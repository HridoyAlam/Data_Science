import re
## one or more digits [0-9]+

x = 'My 2 favorite numbers are 19 and 12'
y = re.findall('[0-9]+', x)
print(y)
z = re.findall('[AEIOU]+',x)
print(z)

## the repeat character (* and +)push outward in both directions
#  (greedy) to match the largest possible string

## one or more characters (^F.+:)
x = 'From: using the: charcters'
m = re.findall('^F.+:',x)
print(m)

## one or more characters (^F.+:) non greedy

n = re.findall('^F.+?:',x)
print(n)

x = 'From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# at least one non-whitespace character '\S+@\S+'
y = re.findall('\S+@\S+', x)
q = re.findall('\S+?@\S+',x)
print("quiz: ",q)
print(y)

n = re.findall('^From (\S+@\S+)',x)
print(n)
atpos = x.find('@')
print(atpos)
sppos = x.find(" ",atpos)
print(sppos)
host = x[atpos+1:sppos]
print(host)

words = x.split()
print(words)
email = words[1]
print(email)
pieces = email.split("@")
print(pieces)
print(pieces[1])

another_way = re.findall('@([^ ]*)', x)
print(another_way)
line = re.findall('^From .*@([^ ]*)',x)
print(line)