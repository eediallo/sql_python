import sqlite3


conn = sqlite3.connect('shop.db')
curr = conn.cursor()


# Create tables
query = 'CREATE TABLE Orders(OrderNo TEXT PRIMARY KEY, Custid TEXT, ProdNo TEXT, Qty INTEGER, FOREIGN KEY(Custid) REFERENCES Customer(Custid), FOREIGN KEY(ProdNo) REFERENCES Product(ProdNo))'
curr.execute(query)
curr.close()
conn.close()