import unittest
import os
from app import create_app, db
from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad

class EspecialidadTestCase(unittest.TestCase):

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

    def test_especialidad_creation(self):
        tipo = TipoEspecialidad(nombre="Especialidad 1", nivel="Avanzado")
        db.session.add(tipo)
        db.session.commit()

        especialidad = Especialidad(
            nombre="Ingeniería de Software",
            letra="IS",
            observacion="Observación de prueba",
            tipo_especialidad_id=tipo.id
        )
        db.session.add(especialidad)
        db.session.commit()

        self.assertIsNotNone(especialidad.id)
        self.assertEqual(especialidad.nombre, "Ingeniería de Software")
        self.assertEqual(especialidad.letra, "IS")
        self.assertEqual(especialidad.tipo_especialidad.nombre, "Especialidad 1")
        self.assertEqual(especialidad.tipo_especialidad.nivel, "Avanzado")

if __name__ == "__main__":
    unittest.main()
