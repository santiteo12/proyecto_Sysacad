import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import config

db = SQLAlchemy()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT', 'development')
    app = Flask(__name__)
    
    # Cargar configuración según entorno
    f = config.factory(app_context)
    app.config.from_object(f)

    # Inicializar base de datos
    db.init_app(app)

    # 🔁 Importar todos los modelos para que SQLAlchemy los registre
    from app.models import (
        grado,
        universidad,
        facultad,
        materia,
        especialidad,
        orientacion,
        plan,
        pais,
        provincia,
        localidad,
    )

    # Contexto interactivo (opcional)
    @app.shell_context_processor    
    def ctx():
        return {"app": app, "db": db}

    return app
