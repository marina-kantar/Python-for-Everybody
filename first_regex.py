import re
name = input('Enter file name: ')
if len(name) <= 1 : name = 'mbox-short.txt'
handle = open(name)
for line in handle:
    line = line.rstrip()
    if re.search ('From: ', line):
        print(line)
