import sqlite3

conexion = sqlite3.connect("basedatos1.db")
cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS set edad = 31 where nombre = 'Carlos'")

conexion.commit()
conexion.close()

#esto es para porbar
#que funciono el cambio en git