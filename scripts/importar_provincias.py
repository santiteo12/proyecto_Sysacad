import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.provincia import Provincia

app = create_app()
xml_path = "xml/provincias.xml"

def importar_provincias(path: str):
    print(f"\n📥 Importando provincias desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} provincias encontradas en el XML")

    nuevas = 0

    with app.app_context():
        for r in registros:
            try:
                provincia_id = int(r.find("provincia").text)
                nombre = r.find("nombre").text.strip()
                pais_id = int(r.find("pais").text)

                if not db.session.get(Provincia, provincia_id):
                    provincia = Provincia(
                        id=provincia_id,
                        nombre=nombre,
                        pais_id=pais_id
                    )
                    db.session.add(provincia)
                    nuevas += 1

            except Exception as e:
                print(f"⚠️ Entrada inválida, se omite: {ET.tostring(r, encoding='unicode').strip()}")
                print(f"   ↳ Error: {e}")
                db.session.rollback()

        db.session.commit()
        print(f"✅ Importación completa. {nuevas} provincias nuevas agregadas.")

if __name__ == "__main__":
    importar_provincias(xml_path)
