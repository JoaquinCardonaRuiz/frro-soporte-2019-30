# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    ssql = "SELECT * from tabla_personas where idPersona=?"
    cursor.execute(ssql, (id_persona,))
    connection.commit()
    res = cursor.fetchone()
    if res is None:
        return False
    else:
        ssql = "UPDATE tabla_personas SET nombre=?, fechaNacimiento=?, dni=?, altura=? "
        cursor.execute(ssql, (nombre, nacimiento, dni, altura,))
        connection.commit()
        return True


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', '15/05/1988', 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', '16/05/1988', 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '16/05/1988', 32165497, 181)
    assert actualizar_persona(123, 'nadie', '16/05/1988', 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
