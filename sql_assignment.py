import sqlite3
import re

conn = sqlite3.connect('domsql.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname)< 1 : fname = 'mbox.txt'
handle = open(fname)

for line in handle :
    line = line.rstrip()
    dom = re.findall('^From:.+@([a-z.]+)', line)
    if len(dom) < 1 : continue
    org = dom[0]
    cur.execute('SELECT count FROM Counts WHERE org= ?', (org,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()

# ogranici na 10
sqlstr = 'SELECT org, count FROM Counts ORDER BY count'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
conn.commit()
   
cur.close()