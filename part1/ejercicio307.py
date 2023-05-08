import sqlite3 #import sqlite3: esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.

conexion=sqlite3.connect("bd1.db")  #esta línea crea una conexión a una base de datos SQLite llamada bd1.db. Si la base de datos no existe, se creará.
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
## Esta línea ejecuta una consulta SQL que selecciona la descripción de los artículos de la tabla "articulos" donde el precio es menor que el precio introducido.
filas=cursor.fetchall()
if len(filas)>0:# Esta línea comprueba si hay filas devueltas por la consulta.
    for fila in filas:# Si hay filas, este bucle itera sobre cada fila.
        print(fila)  #esta línea la imprime.
else:
    print("No existen artículos con un precio menor al ingresado.")# Esta línea imprime un mensaje que indica que no hay artículos con un precio inferior al precio introducido.
conexion.close() #Esta línea cierra la conexión a la base de datos.

