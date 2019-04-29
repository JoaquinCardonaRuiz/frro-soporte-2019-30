# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def buscar_persona(id_persona):
    ssql = "SELECT * FROM tabla_personas where idPersona=?"
    cursor.execute(ssql, (id_persona,))
    res = cursor.fetchone()
    if res is None:
        return False
    else:
        return res


@reset_tabla
def pruebas():
    agregar_persona('juan perez', '15/05/1988', 32165498, 180)
    juan = buscar_persona(1)
    assert juan == (1, 'juan perez',"15/05/1988", 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
