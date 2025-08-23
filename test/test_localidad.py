import unittest
import os
from app import create_app, db
from app.models.localidad import Localidad

class LocalidadTestCase(unittest.TestCase):
    def setUp(self):
        os.environ["FLASK_CONTEXT"] = "testing"
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_localidad_creation(self):
        localidad = Localidad()
        localidad.nombre = "La Plata"
        localidad.codigo_postal = "1900"
        localidad.provincia_id = 1

        self.assertIsNotNone(localidad)
        self.assertEqual(localidad.nombre, "La Plata")
        self.assertEqual(localidad.codigo_postal, "1900")
        self.assertEqual(localidad.provincia_id, 1)

if __name__ == "__main__":
    unittest.main()
