import re
name = input('Enter file name: ')
if len(name) <= 1 : name = 'exp.txt'
handle = open(name)
for line in handle :
    line = line.rstrip()
    y = re.findall('[0-9][0-9][0-9][0-9]* [0-9][0-9][0-9][0-9]* [0-9][0-9][0-9][0-9]*', line)
    if len(y) < 1 : continue
    print(y)