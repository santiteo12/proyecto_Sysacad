import unittest
import os
from app import create_app, db
from app.models.provincia import Provincia

class ProvinciaTestCase(unittest.TestCase):
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

    def test_provincia_creation(self):
        provincia = Provincia()
        provincia.nombre = "Buenos Aires"
        self.assertIsNotNone(provincia)
        self.assertEqual(provincia.nombre, "Buenos Aires")

if __name__ == "__main__":
    unittest.main()
