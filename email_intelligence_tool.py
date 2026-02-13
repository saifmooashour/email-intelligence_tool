import sqlite3
conn = sqlite3.connect('emailtool.db')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Counts;

CREATE TABLE Counts (
    email TEXT PRIMARY KEY,
    count INTEGER NOT NULL
);
''')
fname = input("Enter file name: ").strip()
if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
for line in fhand:
    if not line.startswith('From '):
        continue

    pieces = line.split()
    if len(pieces) < 1:
        continue

    email = pieces[1]

    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
conn.commit()
try:
    top_n = int(input("How many top senders? ").strip())
except:
    top_n = 10

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT ?'
for row in cur.execute(sqlstr, (top_n,)):
    print(row[0], row[1])
cur.close()
conn.close()
