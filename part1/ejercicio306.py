import sqlite3 #import sqlite3: esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.

conexion=sqlite3.connect("bd1.db") 
codigo=int(input("Ingrese el código de un artículo:"))#Esta línea solicita al usuario que ingrese el código de un artículo y almacena el valor ingresado por el usuario como un número entero en la variable codigo.
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
#Esta linea ejecuta una sentencia SQL que selecciona las columnas descripcion y precio de la tabla articulos donde coincide el valor de la columna codigo el valor introducido por el usuario. El resultado de la consulta se almacena en un objeto de cursor.
fila=cursor.fetchone() #Esta línea recupera la primera fila del resultado de la consulta y la almacena en la variable fila.
if fila!=None: #Esta línea comprueba si la consulta devolvió una fila.
    print(fila)#esta línea la imprime.
else:#Si la consulta no devolvió ninguna fila, esta línea inicia un bloque else.
    print("No existe un artículo con dicho código.") #esta línea la imprime.
conexion.close() # conexion.close(): Esta línea cierra la conexión a la base de datos.
