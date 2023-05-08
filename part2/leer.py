import sqlite3#esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.

db_file = 'database.db'
#esta línea define el nombre del archivo de la base de datos SQLite como una cadena y lo asigna a la variable db_file.
with sqlite3.connect(db_file) as conn:
#Esta línea establece una conexión a la base de datos SQLite utilizando el método connect() del módulo sqlite3 y 
# abre un contexto para el objeto de conexión conn. La declaración with garantiza que la conexión se cierre correctamente 
# después de que se ejecute su bloque.
    cursor = conn.cursor()
#Esta línea crea un objeto de cursor para interactuar con la base de datos. El cursor se utiliza para ejecutar consultas SQL y recuperar datos de la base de datos.
    cursor.execute("""
                   select * from images
                   """)
#cursor.execute(""" select * from images """): Esta línea ejecuta una consulta SQL para recuperar todas las filas y columnas de la tabla de 
# imágenes en la base de datos. La consulta se ejecuta usando el método execute() del objeto cursor.
    for row in cursor.fetchall():
#Esta línea recupera todas las filas devueltas por la consulta y las itera una por una usando un bucle for.
        name, size, date = row
#esta línea descomprime los valores de cada fila en tres variables: nombre, tamaño y fecha.
        print(f'{name} {size} {date}')
