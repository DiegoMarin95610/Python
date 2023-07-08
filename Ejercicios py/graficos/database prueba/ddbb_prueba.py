import sqlite3

conection = sqlite3.connect(
    database = "newdb"
)

cur = conection.cursor()

# cur.execute("CREATE TABLE PRODUCTS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECTION VARCHAR(20))") 
# cur.execute("INSERT INTO PRODUCTS VALUES('Balon', 10000, 'Deportes')")

# values = [
#     ('Jarron', 6000, 'Ceramica'),
#     ('Reloj', 20000, 'Accesorios'),
#     ('Cama', 12000, 'Hogar')
# ]

#Excutemany para insertar varios parametros que vienen en un una lista de tuplas
# cur.executemany("INSERT INTO PRODUCTS VALUES (?,?,?)", values)

# for value in values:
#     cur.execute("INSERT INTO PRODUCTS VALUES{}".format(value))

cur.execute("SELECT * FROM PRODUCTS")

products = cur.fetchall()

for product in products:
    print(product)




conection.commit()



conection.close