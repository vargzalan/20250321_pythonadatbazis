import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()

DATABASE= "oscar"

mycursor.execute(f"USE {DATABASE}")

# 2. Feladat
mycursor.execute("""
    SELECT elnyeres_ev, film_eredeti_cim
    FROM oscar_dijak
    ORDER BY elnyeres_ev ASC
""")
myresult = mycursor.fetchall()
print("2. Feladat:")
for x in myresult:
    print(x)

# 3. Feladat
mycursor.execute("""
    SELECT jeloles_ev
    FROM jeloltek
    GROUP BY jeloles_ev
    HAVING COUNT(*) >= 10
""")
myresult = mycursor.fetchall()
print("\n3. Feladat:")
for x in myresult:
    print(x)

# 4. Feladat
mycursor.execute("""
    SELECT film_eredeti_cim
    FROM jeloltek
    WHERE jeloles_ev BETWEEN 1939 AND 1945
      AND bemutatas_magyarorszagon = 1
""")
myresult = mycursor.fetchall()
print("\n4. Feladat:")
for x in myresult:
    print(x)

# 5. Feladat
mycursor.execute("""
    SELECT film_eredeti_cim
    FROM oscar_dijak
    WHERE bemutatas_ev > elnyeres_ev + 10
""")
myresult = mycursor.fetchall()
print("\n5. Feladat:")
for x in myresult:
    print(x)

# 6. Feladat
mycursor.execute("""
    SELECT producer_nev, COUNT(*) AS jelolesek_szama, MAX(jeloles_ev) - MIN(jeloles_ev) AS ev_eltel
    FROM jeloltek
    GROUP BY producer_nev
    HAVING COUNT(*) > 1
""")
myresult = mycursor.fetchall()
print("\n6. Feladat:")
for x in myresult:
    print(x)

# 7. Feladat
mycursor.execute("""
    SELECT DISTINCT producer_nev
    FROM jeloltek
    WHERE film_id IN (
        SELECT film_id
        FROM jeloltek
        WHERE producer_nev = 'Clint Eastwood'
    ) AND producer_nev != 'Clint Eastwood'
""")
myresult = mycursor.fetchall()
print("\n7. Feladat:")
for x in myresult:
    print(x)

# 8. Feladat
mycursor.execute("""
    SELECT producer_nev
    FROM jeloltek
    WHERE film_id NOT IN (
        SELECT film_id
        FROM jeloltek
        WHERE bemutatas_magyarorszagon IS NOT NULL
    )
    GROUP BY producer_nev
""")
myresult = mycursor.fetchall()
print("\n8. Feladat:")
for x in myresult:
    print(x)

mydb.close()
