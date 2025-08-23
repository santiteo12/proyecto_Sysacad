import unittest
from flask import current_app
from app import create_app
from app.models.tipo_documento import TipoDocumento
from app.services import TipoDocumentoService
from app import db
import os

class TipoDocumentoTestCase(unittest.TestCase):

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

    def __nuevoTipoDocumento(self):
        tipo_doc = TipoDocumento()
        tipo_doc.nombre = "DNI"
        tipo_doc.descripcion = "Documento Nacional de Identidad"
        return tipo_doc
    """
    __nuevoTipoDocumento es un método privado que crea una nueva instancia de TipoDocumento con valores predeterminados.
    Se utiliza en las pruebas para crear un objeto TipoDocumento para probar la funcionalidad de TipoDocumentoService.
    """

    def test_tipo_documento_creation(self):
        tipo_doc = self.__nuevoTipoDocumento()
        self.assertIsNotNone(tipo_doc)
        self.assertEqual(tipo_doc.nombre, "DNI")
        self.assertEqual(tipo_doc.descripcion, "Documento Nacional de Identidad")
        
    def test_crear_tipo_documento(self):
        tipo_doc = self.__nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        self.assertIsNotNone(tipo_doc)
        self.assertIsNotNone(tipo_doc.id)
        self.assertGreaterEqual(tipo_doc.id, 1)
        self.assertEqual(tipo_doc.nombre, "DNI")
        
    def test_tipo_documento_busqueda(self):
        tipo_doc = self.__nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc_buscado = TipoDocumentoService.buscar_por_id(tipo_doc.id)
        self.assertIsNotNone(tipo_doc_buscado)
        self.assertEqual(tipo_doc_buscado.nombre, "DNI")
        self.assertEqual(tipo_doc_buscado.descripcion, "Documento Nacional de Identidad")
    
    def test_buscar_tipos_documento(self):
        tipo_doc1 = self.__nuevoTipoDocumento()
        tipo_doc2 = self.__nuevoTipoDocumento()
        tipo_doc2.nombre = "Pasaporte"
        tipo_doc2.descripcion = "Documento para viajes internacionales"
        TipoDocumentoService.crear_tipo_documento(tipo_doc1)
        TipoDocumentoService.crear_tipo_documento(tipo_doc2)
        tipos_doc = TipoDocumentoService.buscar_todos()
        self.assertIsNotNone(tipos_doc)
        self.assertEqual(len(tipos_doc), 2)
        
    def test_actualizar_tipo_documento(self):
        tipo_doc = self.__nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        tipo_doc.descripcion = "DNI Argentino"
        tipo_doc_actualizado = TipoDocumentoService.actualizar_tipo_documento(tipo_doc.id, tipo_doc)
        self.assertEqual(tipo_doc_actualizado.descripcion, "DNI Argentino")
        
    def test_borrar_tipo_documento(self):
        tipo_doc = self.__nuevoTipoDocumento()
        TipoDocumentoService.crear_tipo_documento(tipo_doc)
        db.session.delete(tipo_doc)
        db.session.commit()
        tipo_doc_borrado = TipoDocumentoService.borrar_por_id(tipo_doc.id)
        self.assertIsNone(tipo_doc_borrado)

if __name__ == '__main__':
    unittest.main()