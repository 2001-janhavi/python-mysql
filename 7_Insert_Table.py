import mysql.connector

mydb =  mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testpython"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers(name,address) VALUES (%s,%s)"
val = ("Sakshi","Baner,Pune")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")