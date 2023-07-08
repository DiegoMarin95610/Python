import sqlite3

con = sqlite3.connect("dbproject1")
cur = con.cursor()

# cur.execute('''
#     CREATE TABLE USER(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NAME VARCHAR(40),
#         LAST_NAME VARCHAR(40),
#         CITY VARCHAR(20),
#         EMAIL VARCHAR(30)
#         COMENT VARCHAR(80)
#     )
# ''')


con.close