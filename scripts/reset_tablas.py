import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

app = create_app()

with app.app_context():
    print("❌ Borrando todas las tablas...")
    db.drop_all()
    print("✅ Tablas borradas")

    print("🛠️ Creando todas las tablas...")
    db.create_all()
    print("✅ Tablas creadas")
