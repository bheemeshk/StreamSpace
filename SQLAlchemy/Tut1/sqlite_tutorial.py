__author__ = 'bheem'

import sqlite3

db = sqlite3.connect(':memory:')


cursor = db.cursor()
cursor.execute('''
                CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)
                ''')


#DATA ADDITION MODULE
#INSERTING FIRST USER
cursor.execute('''
                INSERT INTO users(name, phone, email, password)
                VALUES(?, ?, ?, ?)''', ("Bheemesh", "551358", "bk@email.com", "123")

)
print("First User Inserted")


cursor.execute('''
                INSERT INTO users(name, phone, email, password)
                VALUES(?, ?, ?, ?)''', ("Srilakshmi", "523258", "sk@email.com", "123")

)
print("Second User Inserted")



db.commit()



cursor.execute('''
                SELECT * FROM users WHERE id=?
                ''', ("1"))

# cursor.execute('''
#                 SELECT * FROM users
#                 ''')


for row in cursor:
    print('{0} : {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))



