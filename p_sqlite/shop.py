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

query = 'INSERT INTO Product(ProdNo, Pname, Price)VALUES(?, ?, ?)'

products = [
    ('P10', 'Toothpaste', 20.8),
    ('P11', 'ToothBrush', 10.8),
    ('P12', 'Champoo', 88.9),
    ('P13', 'Milk', 9.6),
    ('P14', 'Soap', 5.8),
    ('P15', 'Farime', 34.8),
]

curr.executemany(query, products)
conn.commit()

curr.close()
conn.close()