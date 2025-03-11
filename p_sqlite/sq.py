import sqlite3


conn = sqlite3.connect('forum.db')

curr = conn.cursor()

# curr.execute('CREATE TABLE Students(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, city TEXT, deptno INTEGER, FOREIGN KEY(deptno) REFERENCES Dept(deptno))')

# INSERT DATA
# query = ('INSERT INTO Students (name, city) VALUES (?, ?)')

# students = [
#     ('Elhadj', 'London'),
#     ('Kadi', 'Montreal'),
#     ('Fatim', 'Conakry'),
#     ('Mariam', 'Dakar'),
#     ('Ousmane', 'Paris'),
#     ('Alpha', 'Accra'),
#     ('Fatou', 'Birminghan'),
#     ('Ibrahim', 'Mamou'),
#     ('Abdoul', 'London'),
#     ('Binta', 'Marseille'),
# ]

# curr.executemany(query, students)

# QUERY DATA
# query = 'SELECT * FROM Students'
# curr.execute(query)
# result = curr.fetchall()
# print('============================================')
# print('ID \tNAME\t\tCity')
# print('--- \t----\t\t----')
# for student in result:
#     print(student[0], '\t%s' %student[1], '\t\t%s' %student[2], '\t\t%s' %student[3])
# print('============================================')
# # conn.commit()

# # UPDATE deptno in students
# # Assuming deptno values are from 1 to 10
# for i in range(1, 11):
#     updateQuery = f'UPDATE Students SET deptno = {i} WHERE roll = {i}'
#     curr.execute(updateQuery)
#     conn.commit()


query = 'SELECT * FROM Students WHERE name like "%ab%"'
curr.execute(query)
result = curr.fetchall()
print('============================================')
print('ID \tNAME\t\tCity')
print('--- \t----\t\t----')
for student in result:
    print(student[0], '\t%s' %student[1], '\t\t%s' %student[2])
print('============================================')

curr.close()
conn.close()