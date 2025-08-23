import unittest
import os
from app import create_app, db
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad
from app.models.plan import Plan
from app.models.materia import Materia

class OrientacionTestCase(unittest.TestCase):

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
    
    def test_orientacion_creation(self):
        tipo = TipoEspecialidad(nombre="Especialidad 1", nivel="Avanzado")
        db.session.add(tipo)
        db.session.commit()

        especialidad = Especialidad(nombre="Ingeniería de Software", letra="IS", observacion="Obs", tipo_especialidad_id=tipo.id)
        plan = Plan(nombre="Plan 2023", fecha_inicio="2023-01-01", fecha_fin="2023-12-31", observacion="Plan actual")
        materia = Materia(nombre="Matemáticas", codigo="MAT101")

        db.session.add_all([especialidad, plan, materia])
        db.session.commit()

        orientacion = Orientacion(
            nombre="Orientación de prueba",
            especialidad_id=especialidad.id,
            plan_id=plan.id,
            materia_id=materia.id
        )

        db.session.add(orientacion)
        db.session.commit()

        self.assertIsNotNone(orientacion.id)
        self.assertEqual(orientacion.nombre, "Orientación de prueba")
        self.assertEqual(orientacion.especialidad.nombre, "Ingeniería de Software")
        self.assertEqual(orientacion.plan.nombre, "Plan 2023")
        self.assertEqual(orientacion.materia.nombre, "Matemáticas")

if __name__ == "__main__":
    unittest.main()
