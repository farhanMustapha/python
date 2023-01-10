import sqlite3

class Question:
    def __init__(self,id,numQ):
        self.id=id
        self.numQ=numQ

conn=sqlite3.connect('myDb.db')

cur=conn.cursor()
#req="CREATE TABLE students(id integer primary key autoincrement,nom text,email text,age float)"
req="INSERT INTO students(nom,email,age) values('ahmed','fm@gmail.com',25)"
cur.execute(req)
conn.commit()
conn.close()