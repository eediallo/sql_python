import sqlite3


conn = sqlite3.connect('shop.db')
curr = conn.cursor()


# # Create tables
# query = 'CREATE TABLE Orders(OrderNo TEXT PRIMARY KEY, Custid TEXT, ProdNo TEXT, Qty INTEGER, FOREIGN KEY(Custid) REFERENCES Customer(Custid), FOREIGN KEY(ProdNo) REFERENCES Product(ProdNo))'
# curr.execute(query)

# INSERT INTO TABLE
query = 'INSERT INTO Product(ProdNo, Pname, Price)VALUES(?, ?, ?)'

products = [
    ('P10', 'Haj', 'London Bridge'),
    ('P11', 'Fatma', 'Uxbrigde, Denham'),
    ('P12', 'Donara', 'Mali Yembery'),
    ('P13', 'Naika', 'Ditinn, Fatako'),
    ('P14', 'Rihana', 'Paris, France'),
    ('P15', 'Daniel', 'Madrid, Spain'),
]

curr.executemany(query, products)
conn.commit()

curr.close()
conn.close()