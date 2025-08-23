import unittest
import os
from flask import current_app
from app import create_app
from app.models.tipo_dedicacion import TipoDedicacion

class TipoDedicacionTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        
    def tearDown(self):
        self.app_context.pop()
        
    def test_tipodedicacion_creation(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre= "Simple"
        tipo_dedicacion.observacion = "Observacion 1"
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Simple")
        self.assertIsNotNone(tipo_dedicacion.observacion)
        self.assertEqual(tipo_dedicacion.observacion, "Observacion 1")
        
if __name__ == '__main__':
    unittest.main()