
# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3
from practico_03.ejercicio_01 import borrar_tabla, crear_tabla

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def crear_tabla_peso():
    ssql = 'CREATE TABLE IF NOT EXISTS personaPeso(idPersona INTEGER, fecha DATE, peso INT, FOREIGN KEY(idPersona) REFERENCES tabla_personas(idPersona))'
    cursor.execute(ssql)

def borrar_tabla_peso():
    ssql = 'DROP TABLE IF EXISTS personaPeso'
    cursor.execute(ssql)

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
