import sqlite3


conn = sqlite3.connect('shop.db')
curr = conn.cursor()


# # Create tables
# query = 'CREATE TABLE Orders(OrderNo TEXT PRIMARY KEY, Custid TEXT, ProdNo TEXT, Qty INTEGER, FOREIGN KEY(Custid) REFERENCES Customer(Custid), FOREIGN KEY(ProdNo) REFERENCES Product(ProdNo))'
# curr.execute(query)


# createQuery = 'CREATE TABLE Product(ProdNo TEXT PRIMARY Key, Pname TEXT, Price FLOAT)'
# curr.execute(createQuery)

# INSERT INTO TABLE
# dropQuery = 'DROP TABLE Product'
# curr.execute(dropQuery)

# query = 'INSERT INTO Orders(OrderNo, Custid, ProdNo, Qty)VALUES(?, ?, ?, ?)'

# oders = [
#     (10005, 'P002', 'P15', 8),
#     (10003, 'P001', 'P12', 5),
#     (10006, 'P006', 'P10', 80),
#     (10001, 'P003', 'P11', 30),
#     (10111, 'P004', 'P14', 8),
#     (10020, 'P001', 'P11', 9),
#     (10021, 'P002', 'P10', 29),
#     (11111, 'P002', 'P15', 189),
# ]

# curr.executemany(query, oders)
# conn.commit()
cQuery = ('SELECT * FROM Customer')
curr.execute(cQuery)
result = curr.fetchall()
for customer in result:
    print(customer)
curr.close()
conn.close()