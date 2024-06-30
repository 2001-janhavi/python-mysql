import mysql.connector

mydb = mysql.connector.connect(
   host ="localhost",
   user ="root",
   password ="",
   database="ssi" #if this does not exist, we will get an error
)
print(mydb)