import os
import sys

# Contexto de la app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db

# Crear la app y el contexto
app = create_app()
with app.app_context():
    print("🔧 Creando todas las tablas en la base de datos...")
    db.create_all()
    print("✅ Tablas creadas correctamente.")
