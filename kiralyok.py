from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='mysql',
                                 host='127.0.0.1',
                                 database='kiralyok')

#táblák megjelenítése
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
print("-----")

#uralkodó megjelenítése
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor:
    print(uralkodo)
print("-----")

#matyas kiraly
cursor.execute("SELECT * FROM uralkodo WHERE uralkodo.nev='I. Mátyás'")
for uralkodo in cursor:
    print(uralkodo)   
print("-----")

#matlyas kiral adatai
cursor.execute("SELECT szul,hal FROM uralkodo WHERE uralkodo.nev='I. Mátyás'")
for uralkodo in cursor:
    print(f"Mályás király élt:{uralkodo}")   
print("-----")




cnx.close()