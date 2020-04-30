import re
name = input ('Enter file name: ')
if len(name) <= 1 : name = 'mbox-short.txt'
y = list()
handle = open(name)
for line in handle :
    line = line.rstrip()
    y= y+ re.findall('^From: (\S+@\S+)', line)
    if len(y) < 1 : continue
print(y)
