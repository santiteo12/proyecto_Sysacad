import unittest
import os
from app import create_app, db
from app.models.tipo_especialidad import TipoEspecialidad

class TipoEspecialidadTestCase(unittest.TestCase):

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
    
    def test_tipo_especialidad_creation(self):
        tipo = TipoEspecialidad(nombre="Especialidad 1", nivel="Avanzado")
        db.session.add(tipo)
        db.session.commit()
        self.assertIsNotNone(tipo.id)
        self.assertEqual(tipo.nombre, "Especialidad 1")
        self.assertEqual(tipo.nivel, "Avanzado")

if __name__ == '__main__':
    unittest.main()
