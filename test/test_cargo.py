import unittest
import os
from flask import current_app
from app import create_app
from app.models.cargo import Cargo
from app.models.categoria_cargo import CategoriaCargo

class CargoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_autoridad_creation(self):
        cargo = Cargo()
        cargo.categoria_cargo= CategoriaCargo()
        cargo.categoria_cargo.nombre= "Categoria 1"
        cargo.nombre= "Decano"
        cargo.puntos= 100
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.categoria_cargo)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(cargo.nombre, "Decano")
        self.assertEqual(cargo.puntos, 100)
        
if __name__ == '__main__':
    unittest.main()








