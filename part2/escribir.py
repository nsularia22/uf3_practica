import sqlite3 #esta línea importa el módulo sqlite3, que proporciona una forma de interactuar con las bases de datos SQLite desde Python.
db_filename = 'database.db'
# El script define una variable llamada db_filename, que es el nombre del archivo de la base de datos SQLite.

#El script define una función llamada display_table, que toma un objeto de conexión como argumento. La función crea un objeto de cursor a partir de la conexión, ejecuta una consulta SQL para seleccionar datos de la tabla de imágenes e imprime los datos en un formato tabular.
def display_table(conn):
    cursor = conn.cursor()
    cursor.execute('select name, size, date from images;')
    for name, size, date in cursor.fetchall():
        print(name, size, date)

#El script crea una conexión a la base de datos usando sqlite3.connect. Luego llama a la función Display_Table para imprimir el contenido de la tabla de imágenes.
with sqlite3.connect(db_filename) as conn1:
    print('Before changes:')
    display_table(conn1)

#El script crea un objeto de cursor a partir de la conexión y lo usa para ejecutar una instrucción SQL INSERT para agregar un nuevo registro a la tabla de imágenes.
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into images (name, size, date)
    values ('JournalDev.png', 2000, '2020-02-20');
    """)
#El script vuelve a llamar a la función display_table para imprimir el contenido de la tabla de imágenes después de la instrucción INSERT.
    print('\nAfter changes in conn1:')
    display_table(conn1)


#La secuencia de comandos crea una nueva conexión a la base de datos mediante sqlite3.connect y llama a la función display_table para imprimir el contenido de la tabla de imágenes antes y después de confirmar la instrucción INSERT anterior mediante el método conn1.commit().
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)

# Commit from the first connection
    conn1.commit()
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)
        
#El script crea otra instrucción SQL INSERT para agregar otro registro a la tabla de imágenes.
    cursor1.execute("""
    insert into images (name, size, date)
    values ('Hello.png', 200, '2020-01-18');
    """)
#El script crea otra conexión a la base de datos utilizando sqlite3.connect, llama a la función display_table para imprimir el contenido de 
# la tabla de imágenes antes de que se confirme la declaración INSERT y luego usa conn1.rollback() para revertir la base de datos a 
# su estado anterior. INSERTAR declaración. Finalmente, el script vuelve a llamar a la función display_table para imprimir el contenido 
# de la tabla de imágenes después de la reversión.
    print('\nBefore commit:')
    with sqlite3.connect(db_filename) as conn2:
        
        display_table(conn2)

    # Revert to changes before conn1's commit
    conn1.rollback()
    print('\nAfter connection 1 rollback:')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)
