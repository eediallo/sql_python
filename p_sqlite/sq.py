import sqlite3


conn = sqlite3.connect('forum.db')

curr = conn.cursor()

# curr.execute('CREATE TABLE Students(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, deptno INTEGER, FOREIGN KEY(deptno) REFERENCES Dept(deptno))')

# INSERT DATA
query = ('INSERT INTO Students (name, city) VALUES (?, ?)')

students = [
    ('Elhadj', 'London'),
    ('Kadi', 'Montreal'),
    ('Fatim', 'Conakry'),
    ('Mariam', 'Dakar'),
    ('Ousmane', 'Paris'),
    ('Alpha', 'Accra'),
    ('Fatou', 'Birminghan'),
    ('Ibrahim', 'Mamou'),
    ('Abdoul', 'London'),
    ('Binta', 'Marseille'),
]

curr.executemany(query, students)

conn.commit()

curr.close()
conn.close()