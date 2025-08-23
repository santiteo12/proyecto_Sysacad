import unittest
from flask import current_app
from app import create_app
from app.models.universidad import Universidad
from app.services import UniversidadService
from app import db
import os

class UniversidadTestCase(unittest.TestCase):

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

    def __nuevaUniversidad(self):
        universidad = Universidad()
        universidad.nombre = "Universidad Nacional de La Plata"
        universidad.sigla = "UNLP"
        universidad.domicilio = "Calle 7 N° 776"
        universidad.ciudad = "La Plata"
        universidad.codigo_postal = "1900"
        universidad.telefono = "221-1234567"
        universidad.email = "contacto@unlp.edu.ar"
        return universidad
    """
    __nuevaUniversidad es un método privado que crea una nueva instancia de Universidad con valores predeterminados.
    Se utiliza en las pruebas para crear un objeto Universidad para probar la funcionalidad de UniversidadService.
    """

    def test_universidad_creation(self):
        universidad = self.__nuevaUniversidad()
        self.assertIsNotNone(universidad)
        self.assertEqual(universidad.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad.sigla, "UNLP")
        
    def test_crear_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        self.assertIsNotNone(universidad)
        self.assertIsNotNone(universidad.id)
        self.assertGreaterEqual(universidad.id, 1)
        self.assertEqual(universidad.ciudad, "La Plata")
        
    def test_universidad_busqueda(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        universidad_buscada = UniversidadService.buscar_por_id(universidad.id)
        self.assertIsNotNone(universidad_buscada)
        self.assertEqual(universidad_buscada.nombre, "Universidad Nacional de La Plata")
        self.assertEqual(universidad_buscada.sigla, "UNLP")
    
    def test_buscar_universidades(self):
        universidad1 = self.__nuevaUniversidad()
        universidad2 = self.__nuevaUniversidad()
        universidad2.nombre = "Universidad de Buenos Aires"
        universidad2.sigla = "UBA"
        UniversidadService.crear_universidad(universidad1)
        UniversidadService.crear_universidad(universidad2)
        universidades = UniversidadService.buscar_todos()
        self.assertIsNotNone(universidades)
        self.assertEqual(len(universidades), 2)
        
    def test_actualizar_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        universidad.telefono = "221-7654321"
        universidad_actualizada = UniversidadService.actualizar_universidad(universidad.id, universidad)
        self.assertEqual(universidad_actualizada.telefono, "221-7654321")
        
    def test_borrar_universidad(self):
        universidad = self.__nuevaUniversidad()
        UniversidadService.crear_universidad(universidad)
        db.session.delete(universidad)
        db.session.commit()
        universidad_borrada = UniversidadService.borrar_por_id(universidad.id)
        self.assertIsNone(universidad_borrada)

if __name__ == '__main__':
    unittest.main()