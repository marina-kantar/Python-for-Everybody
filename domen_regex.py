import re
name = input ('Enter file name: ')
if len(name) <= 1 : name = 'mbox-short.txt'
handle = open(name)
y = list()
for line in handle :
    line = line.rstrip()
    y = y+ re.findall('^From.+@(\S+)', line)
    if len(y) < 1 : continue
print(list(set(y)))
