import unittest
from flask import current_app
from app import create_app
from app.models.alumno import Alumno
from app.models.tipo_documento import TipoDocumento
from app.services import AlumnoService
from app import db
import os
from datetime import date

class AlumnoTestCase(unittest.TestCase):

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

    def __nuevoAlumno(self):
        alumno = Alumno()
        alumno.apellido = "Perez"
        alumno.nombre = "Juan"
        alumno.nro_documento = "12345678"
        alumno.tipo_documento = TipoDocumento.DNI
        alumno.fecha_nacimiento = date(1995, 5, 15)
        alumno.sexo = "M"
        alumno.nro_legajo = 1001
        alumno.fecha_ingreso = date.today()
        return alumno
    """
    __nuevoAlumno es un método privado que crea una nueva instancia de Alumno con valores predeterminados.
    Se utiliza en las pruebas para crear un objeto Alumno que se puede utilizar para probar
    la funcionalidad de la clase AlumnoService.
    """

    def test_alumno_creation(self):
        alumno = self.__nuevoAlumno()
        self.assertIsNotNone(alumno)
        self.assertEqual(alumno.apellido, "Perez")
        self.assertEqual(alumno.nro_documento, "12345678")
        self.assertEqual(alumno.tipo_documento, TipoDocumento.DNI)
        
    def test_crear_alumno(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.id)
        self.assertGreaterEqual(alumno.id, 1)
        self.assertEqual(alumno.nro_legajo, 1001)
        
    def test_alumno_busqueda(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        alumno_buscado = AlumnoService.buscar_por_id(alumno.id)
        self.assertIsNotNone(alumno_buscado)
        self.assertEqual(alumno_buscado.apellido, "Perez")
        self.assertEqual(alumno_buscado.nombre, "Juan")
    
    def test_buscar_alumnos(self):
        alumno1 = self.__nuevoAlumno()
        alumno2 = self.__nuevoAlumno()
        alumno2.nro_documento = "87654321"
        AlumnoService.crear_alumno(alumno1)
        AlumnoService.crear_alumno(alumno2)
        alumnos = AlumnoService.buscar_todos()
        self.assertIsNotNone(alumnos)
        self.assertEqual(len(alumnos), 2)
        
    def test_actualizar_alumno(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        alumno.apellido = "Gonzalez"
        alumno_actualizado = AlumnoService.actualizar_alumno(alumno.id, alumno)
        self.assertEqual(alumno_actualizado.apellido, "Gonzalez")
        
    def test_borrar_alumno(self):
        alumno = self.__nuevoAlumno()
        AlumnoService.crear_alumno(alumno)
        db.session.delete(alumno)
        db.session.commit()
        alumno_borrado = AlumnoService.borrar_por_id(alumno.id)
        self.assertIsNone(alumno_borrado)

if __name__ == '__main__':
    unittest.main()