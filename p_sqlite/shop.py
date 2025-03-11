import sqlite3


conn = sqlite3.connect('shop.db')
curr = conn.cursor()




curr.close()
conn.close()