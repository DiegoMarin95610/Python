import sqlite3

con = sqlite3.connect(database="db2prueba")

cur = con.cursor()

# cur.execute('''
#     CREATE TABLE PRODUCTS (
#         ID_ART INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME_ART VARCHAR (32) UNIQUE,
#         PRICE INTEGER,
#         SECTION VARCHAR (15)
#     )
# ''')

#Create
# values = [
#     ('Jarron', 6000, 'Ceramica'),
#     ('Reloj', 20000, 'Accesorios'),
#     ('Cama', 12000, 'Hogar'),
#     ('Sofa', 12000, 'Hogar'),
#     ('Silla', 12000, 'Hogar'),
#     ('Closet', 12000, 'Hogar'),
#     ('Patin', 12000, 'Juegueteria')
# ]
# cur.executemany("INSERT INTO PRODUCTS VALUES (NULL, ?,?,?)", values)

#Read
# cur.execute("SELECT * FROM PRODUCTS")
# product = cur.fetchall()
# print(product)

#Update
cur.execute("UPDATE PRODUCTS SET PRICE = 35 WHERE PRICE = 12000")

#Delete
cur.execute("DELETE FROM PRODUCTS WHERE PRICE = 35")




con.commit()

con.close()