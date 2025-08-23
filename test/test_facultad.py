import unittest
import os
from app import create_app, db
from app.models import Facultad

class FacultadTestCase(unittest.TestCase):

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

    def nueva_facultad(self):
        return Facultad(
            nombre="Facultad de Ciencias Exactas",
            abreviatura="FCE",
            directorio="Ciencias Exactas",
            sigla="FCE",
            codigo_postal="12345",
            ciudad="La Plata",
            domicilio="Calle 123",
            telefono="123456789",
            contacto="Juan Perez",
            email="abc@gmail.com"
        )

    def test_facultad_creation(self):
        facultad = self.nueva_facultad()
        db.session.add(facultad)
        db.session.commit()
        self.assertIsNotNone(facultad.id)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")

    def test_facultad_equality(self):
        f1 = self.nueva_facultad()
        f2 = self.nueva_facultad()
        self.assertNotEqual(f1, f2)  # Son instancias distintas con distinto id

    def test_facultad_repr(self):
        facultad = self.nueva_facultad()
        db.session.add(facultad)
        db.session.commit()
        self.assertIn("Facultad", repr(facultad))

if __name__ == "__main__":
    unittest.main()
