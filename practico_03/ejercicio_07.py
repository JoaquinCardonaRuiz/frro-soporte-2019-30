# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import sqlite3,datetime

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_04 import buscar_persona

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

def existe_posterior_pesaje(id_persona, fecha):
    ssql = "SELECT idPersona FROM personaPeso WHERE idPersona=? and fecha>? "
    cursor.execute(ssql,(id_persona,fecha,))
    res = cursor.fetchone()
    return(res is not None)

def agregar_peso(id_persona,fecha,peso):
    per = buscar_persona(id_persona)
    if (per is not False):
        if existe_posterior_pesaje(id_persona,fecha) is False:
            ssql = "INSERT INTO personaPeso(idPersona,fecha,peso) VALUES(?,?,?)"
            cursor.execute(ssql,(id_persona,fecha,peso,))
            connection.commit()
            return cursor.lastrowid
        else:
            return False
    else:
        return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988,5,15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.date(2018,5,26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.date(1998,5,15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.date(2018,5,16), 80) == False

if __name__ == '__main__':
    pruebas()
