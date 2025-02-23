import sqlite3

conn = sqlite3.connect('alchemy/test.db')
print("Opened database successfully")

#conn.execute("INSERT INTO PERSON (ID,NAME,AGE,ADDRESS,COUNTRY) \
#      VALUES (99, 'Mark', 'Rich-Mond')")
#conn.commit()
#print("Records created successfully")

cursor = conn.execute("SELECT * from user")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
print("Operation done successfully")

conn.execute("UPDATE user set NAME = 'gugug' where ID = 1")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

#conn.execute("DELETE from PERSON where ID = 2;")
#conn.commit()
#print("Total number of rows deleted :", conn.total_changes)


conn.close()
