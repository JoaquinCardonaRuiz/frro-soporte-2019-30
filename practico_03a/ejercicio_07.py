import datetime
from practico_03A.ejercicio_01 import  Persona
from practico_03A.ejercicio_02 import agregar_persona
from practico_03A.ejercicio_04 import buscar_persona
from practico_03A.ejercicio_06 import reset_tabla, PersonaPeso
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


def agregar_peso(id_persona, fecha, peso):
    aux = buscar_persona(id_persona)
    if (aux != False):
        s = session.query(PersonaPeso).filter(PersonaPeso.id_persona == id_persona).filter(PersonaPeso.fecha > fecha).first()
        if (s != None):
            return False
        else:
            p = PersonaPeso()
            p.fecha = fecha
            p.peso = peso
            p.id_persona = id_persona
            session.add(p)
            session.commit()
            return p.id_peso
    else:
        return False

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
