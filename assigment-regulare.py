import re
y = list()
zbir = 0
name = input('Enter file name: ')
if len(name) <=1 : name = 'regex_sum_468299.txt'
handle = open(name)
for line in handle :
    line = line.rstrip()
    y=y+ re.findall('[0-9]+', line)
#print(y)
for i in y :
    zbir = zbir + int(i)
print(zbir)
