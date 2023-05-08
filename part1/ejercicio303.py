import sqlite3 #import sqlite3: esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.

conexion=sqlite3.connect("bd1.db") #conexion=sqlite3.connect("bd1.db"): esta línea crea una conexión a una base de datos SQLite llamada bd1.db. Si la base de datos no existe, se creará.
try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
#conexion.execute("""create table articulos (codigo integer primary key autoincrement, 
#descripcion text, precio real )"""): Esta linea ejecuta una sentencia SQL que crea una tabla llamada articulos con tres columnas: 
# codigo, descripcion y precio. La columna de código es un número entero y es la clave principal de la tabla. 
# También está configurado para autoincrementarse. La columna descripción es de tipo texto y la columna precio es de tipo real.
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    #sqlite3.OperationalError:: esta línea inicia un bloque excepto que detecta excepciones de tipo sqlite3.OperationalError.
    print("La tabla articulos ya existe")
conexion.close()
# conexion.close(): Esta línea cierra la conexión a la base de datos.

