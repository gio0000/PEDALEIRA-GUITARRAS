import sqlite3

conn=sqlite3.connect("efeitos.db")
cursor=conn.cursor()

cursor.execute("""CREATE TABLE SALVOS(
               id INTEGER PRIMARY KEY,
               pitch INTEGER ,
               reverb INTEGER ,
               delay INTEGER ,
               compressor INTEGER ,
               distorcao INTEGER ,
               ganho INTEGER ,
               razao INTEGER ,
               volume INTEGER );""")

conn.commit()
conn.close()
