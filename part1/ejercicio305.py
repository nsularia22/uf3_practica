import sqlite3#esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.

conexion=sqlite3.connect("bd1.db") #esta línea crea una conexión a una base de datos SQLite llamada bd1.db. Si la base de datos no existe, se creará.
cursor=conexion.execute("select codigo,descripcion,precio from articulos") 
# Esta linea ejecuta una sentencia SQL que selecciona las columnas codigo, descripcion y precio de la tabla articulos. El resultado de la consulta se almacena en un objeto de cursor.
for fila in cursor:#Esta línea inicia un ciclo for que itera sobre las filas devueltas por la consulta.
    print(fila) #esta línea la imprime.
conexion.close() # conexion.close(): Esta línea cierra la conexión a la base de datos.


