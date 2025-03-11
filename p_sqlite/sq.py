import sqlite3


conn = sqlite3.connect('forum.db')

curr = conn.cursor()

# curr.execute('CREATE TABLE Students(roll INTEGER PRIMARY Key AUTO_INCREMENT, name TEXT,city TEXT, deptno INTEGER, FOREIGN Key(deptno) references Dept(deptno))')

# INSERT DATA

query = 'INSERT INTO Dept(name) VALUES(?)'
students = [
    ('Economics',),
    ('Science',),
    ('Biology',),
    ('IT',),
]

curr.executemany(query, students)
conn.commit()

curr.close()
conn.close()