import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

#adatbázis létrehozás
DATABASE= "mydatabase"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

#adatbázisok mutatása
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

#használd ezt az adatbázist
mycursor.execute(f"USE {DATABASE}")

#customers tábla létrehozása
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")
print("----")

#táblák mutatása
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

