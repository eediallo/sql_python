import sqlite3


conn = sqlite3.connect('forum.db')

curr = conn.cursor()

# curr.execute('CREATE TABLE Students(roll INTEGER PRIMARY Key AUTO_INCREMENT, name TEXT,city TEXT, deptno INTEGER, FOREIGN Key(deptno) references Dept(deptno))')

# INSERT DATA
dname = input('Enter the Dept name: ')
curr.execute('INSERT INTO Dept (name) VALUES (?)', (dname,))

conn.commit()

curr.close()
conn.close()