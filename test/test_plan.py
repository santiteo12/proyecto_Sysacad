import unittest
import os
from app import create_app, db
from app.models.plan import Plan

class PlanTestCase(unittest.TestCase):

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
    
    def test_plan_creation(self):
        plan = Plan(
            nombre="Plan de Prueba",
            fecha_inicio="2023-01-01",
            fecha_fin="2023-12-31",
            observacion="Este es un plan de prueba."
        )
        db.session.add(plan)
        db.session.commit()

        self.assertIsNotNone(plan.id)
        self.assertEqual(plan.nombre, "Plan de Prueba")
        self.assertEqual(plan.fecha_inicio, "2023-01-01")
        self.assertEqual(plan.fecha_fin, "2023-12-31")
        self.assertEqual(plan.observacion, "Este es un plan de prueba.")

if __name__ == "__main__":
    unittest.main()
