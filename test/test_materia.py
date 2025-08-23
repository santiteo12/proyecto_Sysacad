import unittest
import os
from app import create_app, db
from app.models.materia import Materia
from app.services import MateriaService

class MateriaTestCase(unittest.TestCase):

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
    
    def __nuevaMateria(self):
        return Materia(nombre="Matemáticas", codigo="MAT101")

    def test_materia_creation(self):
        materia = self.__nuevaMateria()
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matemáticas")
        self.assertEqual(materia.codigo, "MAT101")

    def test_crear_materia(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        self.assertIsNotNone(materia.id)
        self.assertEqual(materia.nombre, "Matemáticas")
        
    def test_materia_busqueda(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        encontrada = MateriaService.buscar_por_id(materia.id)
        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada.nombre, "Matemáticas")
        self.assertEqual(encontrada.codigo, "MAT101")
    
    def test_buscar_materias(self):
        materia1 = self.__nuevaMateria()
        materia2 = Materia(nombre="Álgebra", codigo="MAT102")
        MateriaService.crear_materia(materia1)
        MateriaService.crear_materia(materia2)
        materias = MateriaService.buscar_todos()
        self.assertEqual(len(materias), 2)

    def test_actualizar_materia(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        materia.nombre = "Matemáticas Avanzadas"
        actualizada = MateriaService.actualizar_materia(materia.id, materia)
        self.assertEqual(actualizada.nombre, "Matemáticas Avanzadas")

    def test_borrar_materia(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        MateriaService.borrar_por_id(materia.id)
        resultado = MateriaService.buscar_por_id(materia.id)
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()
