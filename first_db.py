import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor ()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstone', 20))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur :
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 19')
conn.commit()
print('New Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur :
    print(row)
conn.close()