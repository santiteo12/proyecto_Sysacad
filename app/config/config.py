from pathlib import Path
import os
from dotenv import load_dotenv

# Base directory del proyecto
basedir = os.path.abspath(Path(__file__).parents[2])

# Cargar variables de entorno desde .env
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI', 'postgresql://user:password@localhost/prod_sysacad')

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Factory para seleccionar configuración según entorno
def factory(env: str) -> Config:
    config_map = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestConfig
    }
    return config_map.get(env, DevelopmentConfig)
