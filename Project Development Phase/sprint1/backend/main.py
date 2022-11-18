import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE users (email TEXT, pass TEXT)')
conn.close()
conn.close()
