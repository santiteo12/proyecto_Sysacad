import unittest
import os
from flask import current_app
from app import create_app
from app.models.area import Area
from app.services import AreaService
from app import db

class   AreaTestCase(unittest.TestCase):
 
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
    

    def nueva_area(self):
        area = Area()
        area.nombre = "Area de Prueba"
        return area

    def test_area_creation(self):
        area= self.nueva_area()
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Area de Prueba")

    def test_crear_area(self):
        area = self.nueva_area()
        AreaService.crear(area)
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.id)
        self.assertEqual(area.nombre, "Area de Prueba")
        self.assertGreaterEqual(area.id, 1)

    def test_area_busqueda(self):
        area = self.nueva_area()
        AreaService.crear(area)
        AreaService.buscar_por_id(area.id)
        self.assertIsNotNone(area)
        self.assertEqual(area.nombre, "Area de Prueba")


    def test_buscar_areas(self):
        area1 = self.nueva_area()
        area2 = self.nueva_area()
        AreaService.crear(area1)
        AreaService.crear(area2)
        areas = AreaService.buscar_todos()
        self.assertIsNotNone(areas)
        self.assertEqual(len(areas), 2)



    def test_actualizar_area(self):
        area = self.nueva_area()
        AreaService.crear(area)
        area.nombre = "Area Actualizada"
        area_actualizada = AreaService.actualizar(area.id, area)
        self.assertEqual(area_actualizada.nombre, "Area Actualizada")



    def test_borrar_area(self):
        area = self.nueva_area()
        AreaService.crear(area)
        db.session.delete(area)
        db.session.commit()
        area_borrada = AreaService.borrar_por_id(area.id)
        self.assertIsNone(area_borrada)

if __name__ == "__main__":
    unittest.main()