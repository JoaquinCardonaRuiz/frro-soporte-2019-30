# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime, sqlite3

from practico_03.ejercicio_01 import reset_tabla

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def agregar_persona(nombre, nacimiento, dni, altura):

    ssql = "INSERT INTO tabla_personas(nombre , fechaNacimiento , dni , altura ) VALUES (?,?,?,?)"
    cursor.execute(ssql, (nombre,nacimiento,dni,altura,))
    connection.commit()

    return cursor.lastrowid

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez','15/5/1988', 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez','25/01/1980', 12164492, 195)
    assert id_juan == 1
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
