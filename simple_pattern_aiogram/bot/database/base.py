import sqlite3
import os

os.chdir(os.path.dirname(__file__)) # make sure

conn = sqlite3.connect('mydb.db') # connect to


cursor = conn.cursor() # create a cursor
raw_query = """
CREATE TABLE IF NOT EXISTS products 
    (
        id INT PRIMARY KEY, 
        title TEXT NOT NULL,
        description TEXT,
        price REAL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
cursor.execute(raw_query) # execute query
conn.commit() # commit the transaction

raw_query_1 = """
INSERT INTO products (title, description, price) VALUES 
(?, ?, ?)""" 

cursor.execute(raw_query_1, ('iPhone X', 'This is Smartphone', 32000.12)) # execute query
conn.commit() # commit the transaction

conn.close() # close the connection



