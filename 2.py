import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="root")
x=int(input("Enter the rollno: "))
cur=connection.cursor()
cur.execute("USE TEST")
cur.execute("SELECT * FROM STUDENT WHERE ROLLNO = {}".format(x))
print(cur.fetchall())
connection.close()