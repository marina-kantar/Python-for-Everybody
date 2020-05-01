d = {'a' : 2 , 'c' : 1 , 'd' : 4, 'b' : 3}
t =d.items()
print(t)
s = sorted(d.items())
print(s)
for i, v in sorted(d.items()) :
    print(i, v)
o = list()
for i,v in d.items():
    o.append((v, i))
print(o)
o= sorted(o, reverse=True)
