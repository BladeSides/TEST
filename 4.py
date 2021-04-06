import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="root")
cur=connection.cursor()
cur.execute("USE TEST")
cur.execute("SELECT * FROM STUDENT WHERE PROJECT = 'SUBMITTED' OR PROJECT = 'EVALUATED'");
x=cur.fetchall()
for y in x:
    print(y)
connection.close()