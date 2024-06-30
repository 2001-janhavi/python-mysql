import mysql.connector

mydb =  mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testpython"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD column id INT AUTO_INCREMENT PRIMARY KEY")