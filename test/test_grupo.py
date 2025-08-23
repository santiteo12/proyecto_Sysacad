import unittest
import os
from flask import current_app
from app import create_app
from app.models.grupo import Grupo

class   GrupoTestCase(unittest.TestCase):
 
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_grupo_creation(self):
        area= Grupo()
        


if __name__ == "__main__":
    unittest.main()