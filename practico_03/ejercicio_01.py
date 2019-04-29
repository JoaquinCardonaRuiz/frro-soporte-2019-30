# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def crear_tabla():
    ssql = 'CREATE TABLE IF NOT EXISTS tabla_personas(idPersona INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, fechaNacimiento DATE, dni INT, altura INT)'
    cursor.execute(ssql)

def borrar_tabla():
    ssql = 'DROP TABLE IF EXISTS tabla_personas'
    cursor.execute(ssql)

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
