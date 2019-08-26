import unittest

from p_05.ejercicio_01 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        self.assertEqual(len(self.ns.todos()), 0)
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        invalido = Socio(dni=12345678, nombre='', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        invalido = Socio(dni=12345678, nombre='Juan'*20, apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        invalido = Socio(dni=12345678, nombre='Juan', apellido='')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez'*20)
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.regla_3())
        for y in range(0, 200):
            invalido = Socio(nombre='Juan', apellido='Perez')
            self.ns.alta(invalido)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3())

    def test_baja(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.baja(valido.id_socio))
        invalido = Socio(dni = 12345789, nombre='Juan', apellido='Perez')
        self.ns.baja(invalido)
        self.assertFalse(self.ns.baja(invalido.id_socio))

    def test_buscar(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.buscar(valido.id_socio))
        invalido = Socio(dni=87654321, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.buscar(invalido.id_socio))


    def test_buscar_dni(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        self.assertTrue(self.ns.buscar_dni(valido.dni))
        invalido = Socio(dni=87654321, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.buscar_dni(invalido.dni))

    def test_todos(self):
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        assert self.ns.todos() != None 

    def test_modificacion(self):
        valido = valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(valido)
        valido_mod = Socio(dni=12345679, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.modificacion(valido_mod))
        invalido = Socio(dni=87654321, nombre='Juan', apellido='Perez')
        self.assertFalse(self.ns.modificacion(invalido))
