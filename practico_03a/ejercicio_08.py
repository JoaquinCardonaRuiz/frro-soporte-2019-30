import datetime
from practico_03A.ejercicio_01 import reset_tabla, Persona
from practico_03A.ejercicio_02 import agregar_persona
from practico_03A.ejercicio_04 import buscar_persona
from practico_03A.ejercicio_06 import reset_tabla, PersonaPeso
from practico_03A.ejercicio_07 import agregar_peso
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime
from practico_03A.ejercicio_01 import borrar_tabla, crear_tabla
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
engine = create_engine('sqlite:///personas.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def listar_pesos(id_persona):
    aux = buscar_persona(id_persona)
    if (aux != False):
        ps = session.query(PersonaPeso).filter(PersonaPeso.id_persona == id_persona).all()
        lista = []
        for p in ps:
            lista.append((p.fecha,p.peso))
        return lista
    else:
        return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
