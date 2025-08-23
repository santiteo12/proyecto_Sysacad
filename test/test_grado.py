import unittest
import os
from flask import current_app
from app import create_app, db
from app.models.grado import Grado

class GradoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_grado_creation(self):
        nuevo_grado = Grado(id=1, nombre="Grado de prueba")
        db.session.add(nuevo_grado)
        db.session.commit()

        grado = Grado.query.get(1)
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre, "Grado de prueba")


if __name__ == "__main__":
    unittest.main()
