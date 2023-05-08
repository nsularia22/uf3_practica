#Este es un script de Python que importa los módulos sqlite3 y os, define una función llamada check_db y crea una tabla de base de datos usando SQL.
import sqlite3
import os
#El script importa los módulos sqlite3 y os.
def check_db(filename):
    return os.path.exists(filename)
#La función check_db toma un nombre de archivo y devuelve un valor booleano que indica si el archivo existe o no.
db_file = 'database.db'
schema_file = 'schema.sql'
#El script define dos variables: db_file y schema_file. db_file es el nombre del archivo de la base de datos SQLite que creará el script y schema_file es el nombre del archivo que contiene el esquema SQL para la base de datos.
if check_db(db_file):
    print('Database already exists. Exiting...')
    exit(0)
#El script comprueba si el archivo de la base de datos ya existe mediante la función check_db. Si el archivo existe, el script imprime un mensaje y sale con un código de estado de 0.
with open(schema_file, 'r') as rf:
    # Read the schema from the file
    schema = rf.read()
#El script abre schema_file para lectura, lee el contenido del archivo en la variable de esquema y cierra el archivo.
with sqlite3.connect(db_file) as conn:
    print('Created the connection!')
    # Execute the SQL query to create the table
    conn.executescript(schema)
    print('Created the Table! Now inserting')
    conn.executescript("""
                       insert into images (name, size, date)
                       values
                       ('sample.png', 100, '2019-10-10'),
                       ('ask_python.png', 450, '2019-05-02'),
                       ('class_room.jpeg', 1200, '2018-04-07');
                       """)
    print('Inserted values into the table!')
print('Closed the connection!')
