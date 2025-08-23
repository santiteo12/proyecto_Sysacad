import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.pais import Pais

class PaisTestCase(unittest.TestCase):

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
    
    def test_pais_creation(self):
        pais = Pais()
        pais.id = 12
        pais.nombre = "ARGENTINA"
        self.assertIsNotNone(pais)
        self.assertEqual(pais.id, 12)
        self.assertEqual(pais.nombre, "ARGENTINA")

if __name__ == "__main__":
    unittest.main()
