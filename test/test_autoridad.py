import unittest
import os
from flask import current_app
from app import create_app
from app.models.autoridad import Autoridad
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion

from app.services import AutoridadService
from app import db

class AutoridadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
                
    def tearDown(self): 
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        tipo_dedicacion = TipoDedicacion()
        cargo.nombre= "Decano"
        cargo.puntos= 100
        self.__new_object(autoridad, cargo, tipo_dedicacion)
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertIsNotNone(autoridad.cargo)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "abc@gmail.com")
        self.assertIsNotNone(autoridad.cargo.categoria_cargo)
        self.assertEqual(autoridad.cargo.categoria_cargo.nombre, "Categoria 1")

    def __new_object(self, autoridad, cargo, tipo_dedicacion):
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.tipo_dedicacion = tipo_dedicacion
        cargo.tipo_dedicacion.nombre = "Simple"
        cargo.tipo_dedicacion.observacion = "Observacion 1"
        autoridad.nombre = "Juan Perez"
        autoridad.cargo= cargo
        autoridad.telefono= "123456789"
        autoridad.email= "abc@gmail.com"
        
if __name__ == '__main__':
    unittest.main()










