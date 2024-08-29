import sqlite3
con = sqlite3.connect('c:/sqlite3/collage209.db')
cur = con.cursor()
print("Connection created")
cur.execute("DROP TABLE IF EXISTS faculty")
cur.execute("DROP TABLE IF EXISTS faculty1")
cur.execute("DROP TABLE IF EXISTS faculty2")
cur.execute("DROP TABLE IF EXISTS faculty3")

cur.execute("""
CREATE TABLE faculty (
    fid INT,
    fname VARCHAR(255) NOT NULL
)
""")
cur.execute("""
CREATE TABLE faculty1 (
    fid INT,
    fname VARCHAR(255) NOT NULL
)
""")

cur.execute("""
CREATE TABLE faculty2 (
    fid INT,
    fname VARCHAR(255) NOT NULL
)
""")
cur.execute("""
CREATE TABLE faculty3 (
    fid INT,
    fname VARCHAR(255) NOT NULL
)
""")
con.commit()
print("Tables created")
cur.execute('''INSERT INTO faculty  VALUES('VISHVA',90000)''')
cur.execute('''INSERT INTO faculty  VALUES('NISHI',40000)''')
cur.execute('''INSERT INTO faculty  VALUES('NISHA',50500)''')
cur.execute('''INSERT INTO faculty  VALUES('BHALU',20000)''')
cur.execute('''INSERT INTO faculty  VALUES('MINI',3000)''')
newfaculty=cur.execute("SELECT * FROM faculty")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.execute('''INSERT INTO faculty  VALUES(301,'BAC')''')
cur.execute('''INSERT INTO faculty  VALUES(302,'BBA')''')
cur.execute('''INSERT INTO faculty  VALUES(303,'MCA')''')
cur.execute('''INSERT INTO faculty  VALUES(304,'MBA')''')
cur.execute('''INSERT INTO faculty  VALUES(305,'IT')''')
view=cursor.execute('''SELECT*FROM CURSOR''')
    

