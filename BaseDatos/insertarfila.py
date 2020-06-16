import sqlite3

conexion = sqlite3.connect("basedatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Carlos', 'Trujillo', 'Canales', 30)")

conexion.commit()

conexion.close()