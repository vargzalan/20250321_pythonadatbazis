import mysql.connector

# Kapcsolódás a MySQL adatbázishoz
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql",
  database="mydatabase"
)

cursor = mydb.cursor()

print("1. feladat: Oscar-díjas filmek")
cursor.execute("SELECT cim, ev FROM film WHERE nyert = 1")
for row in cursor.fetchall():
    print(row)

print("\n2. feladat: Legtöbb Oscart nyert film")
cursor.execute("""
    SELECT cim, COUNT(*) as db
    FROM film
    WHERE nyert = 1
    GROUP BY cim
    ORDER BY db DESC
    LIMIT 1
""")
print(cursor.fetchone())

print("\n3. feladat: Filmek száma évenként")
cursor.execute("SELECT ev, COUNT(*) FROM film GROUP BY ev ORDER BY ev")
for row in cursor.fetchall():
    print(row)

print("\n4. feladat: Szereplők listázása")
cursor.execute("SELECT nev FROM keszito")
for row in cursor.fetchall():
    print(row)

print("\n5. feladat: Nem nyert Oscar-díjat")
cursor.execute("SELECT cim FROM film WHERE nyert = 0")
for row in cursor.fetchall():
    print(row)

print("\n6. feladat: Legkorábban bemutatott film")
cursor.execute("SELECT cim, bemutato FROM film ORDER BY bemutato ASC LIMIT 1")
print(cursor.fetchone())

print("\n7. feladat: Legtöbb filmben szereplő színész")
cursor.execute("""
    SELECT keszito.nev, COUNT(*) as db
    FROM kapcsolat
    JOIN keszito ON kapcsolat.keszitoid = keszito.id
    GROUP BY keszitoid
    ORDER BY db DESC
    LIMIT 1
""")
print(cursor.fetchone())

print("\n8. feladat: Adott év Oscar-díjas filmjei (pl. 1994)")
ev = 1994
cursor.execute("SELECT cim FROM film WHERE nyert = 1 AND ev = %s", (ev,))
for row in cursor.fetchall():
    print(row)

print("\n9. feladat: Egy színész és az általa szerepelt filmek")
nev = "Tom Hanks"
cursor.execute("""
    SELECT film.cim
    FROM kapcsolat
    JOIN keszito ON kapcsolat.keszitoid = keszito.id
    JOIN film ON kapcsolat.filmid = film.id
    WHERE keszito.nev = %s
""", (nev,))
for row in cursor.fetchall():
    print(row)

print("\n10. feladat: Toplista filmek száma egy időszakban (pl. 1990-2000)")
start, end = 1990, 2000
cursor.execute("""
    SELECT keszito.nev, COUNT(*) as db
    FROM kapcsolat
    JOIN keszito ON kapcsolat.keszitoid = keszito.id
    JOIN film ON kapcsolat.filmid = film.id
    WHERE film.ev BETWEEN %s AND %s
    GROUP BY keszito.nev
    ORDER BY db DESC
    LIMIT 5
""", (start, end))
for row in cursor.fetchall():
    print(row)

mydb.close()


