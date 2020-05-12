import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, counts INTEGER)')

fname = input('Enter file name: ')
if len(fname)< 1 : fname = 'mbox-short.txt'
handle = open(fname)

for line in handle :
    if not line.startswith('From: ') : continue
    piece = line.split()
    email = piece[1]
    cur.execute('SELECT counts FROM Counts WHERE email= ?', (email,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (email, counts) VALUES (?, 1)', (email,))
    else :
        cur.execute('UPDATE Counts SET counts = counts + 1 WHERE email = ?', (email,))
    conn.commit()

# ogranici na 10
sqlstr = 'SELECT email, counts FROM Counts ORDER BY counts DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
   
cur.close()