import mysql.connector

# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="ediallo98@",
    database = 'dbtest0'
    )


my_curser = cnx.cursor()
# my_curser.execute("CREATE DATABASE testbd")
# for i in range(5):
#     my_curser.execute(f'CREATE DATABASE dbtest{i}')

# my_curser.execute('SHOW DATABASES')
# for db in my_curser:
#     print(db[0])

# my_curser.execute("CREATE TABLE users( name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

# my_curser.execute('SHOW TABLES')
# for table in my_curser:
#     print(table[0])

# sqlstuff = "INSERT INTO users (name, email, age) VALUES(%s, %s, %s)"
# record1  =("Elhadj Abdoul Diallo", "ediallo98@gmail.com", 40)
# my_curser.execute(sqlstuff, record1)
# cnx.commit()


# sqlstuff = "INSERT INTO users (name, email, age) VALUES(%s, %s, %s)"
# records  = [
#     ("Kadi", "kadi@gmail.com", 40),
#     ("Fatim", "fatim@gmail.com", 34),
#     ("Alex", "alex@gmail.com", 50),
#     ("Mick", "mick@gmail.com", 77),

# ]
# my_curser.executemany(sqlstuff, records)

# cnx.commit()

# my_curser.execute('SELECT * FROM users')
# print('NAME\t\tEMAIL\t\t\t\tAGE\t\tID')
# print('----\t\t-----\t\t\t\t---\t\t---')
# result = my_curser.fetchall()
# for row in result:
#     print(row[0], '\t\t%s' %row[1], '\t\t%s' %row[2], '\t\t%s' %row[3])


# WHERE LIKE and Wildcards
# my_curser.execute('SELECT * FROM users WHERE name LIKE "%at%"')
# print('NAME\t\tEMAIL\t\t\t\tAGE\t\tID')
# print('----\t\t-----\t\t\t\t---\t\t---')
# result = my_curser.fetchall()
# for row in result:
#         print(row[0], '\t\t%s' %row[1], '\t\t%s' %row[2], '\t\t%s' %row[3])

# AND / OR clause
# my_curser.execute('SELECT * FROM users WHERE name LIKE "%at%" OR age < 30')
# print('NAME\t\tEMAIL\t\t\t\tAGE\t\tID')
# print('----\t\t-----\t\t\t\t---\t\t---')
# result = my_curser.fetchall()
# for row in result:
#         print(row[0], '\t\t%s' %row[1], '\t\t%s' %row[2], '\t\t%s' %row[3])



# Updating records
my_sql = "UPDATE users SET age = 40 WHERE user_id = 13"
my_curser.execute(my_sql )
cnx.commit()