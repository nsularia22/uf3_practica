import sqlite3 #import sqlite3: esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.

conexion=sqlite3.connect("bd1.db") # conexion=sqlite3.connect("bd1.db"): esta línea crea una conexión a una base de datos SQLite llamada bd1.db. Si la base de datos no existe, se creará.
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50)) #conexion.execute("insertar en articulos(descripcion,precio) valores (?,?)", ("naranjas", 23.50)): Esta linea ejecuta una sentencia SQL que inserta una nueva fila en la tabla articulos con los valores naranjas para la columna descripcion y 23,50 para la columna de precio.
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34)) # conexion.execute("insertar en articulos(descripcion,precio) valores (?,?)", ("peras", 34)): Esta linea ejecuta una sentencia SQL que inserta una nueva fila en la tabla articulos con los valores peras para la columna descripción y 34 para la columna precio.
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25)) # conexion.execute("insertar en articulos(descripcion,precio) valores (?,?)", ("bananas", 25)): Esta linea ejecuta una sentencia SQL que inserta una nueva fila en la tabla articulos con los valores bananas para la columna descripción y 25 para la columna precio.
conexion.commit()#conexion.commit(): Esta línea confirma los cambios realizados en la base de datos. Esto es necesario porque SQLite usa transacciones para garantizar la coherencia de los datos.
conexion.close() # conexion.close(): Esta línea cierra la conexión a la base de datos.

