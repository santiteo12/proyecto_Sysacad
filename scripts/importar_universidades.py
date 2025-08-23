import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.universidad import Universidad

app = create_app()
xml_path = "xml/universidad.xml"

def importar_universidades(path: str):
    print(f"\n📥 Importando universidades desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} universidades encontradas en el XML")

    with app.app_context():
        for r in registros:
            id_elem = r.find("universida")
            nombre_elem = r.find("nombre")

            if id_elem is None or nombre_elem is None:
                print("⚠️ Entrada inválida, se omite:", ET.tostring(r, encoding="unicode"))
                continue

            universidad_id = int(id_elem.text)
            nombre = nombre_elem.text.strip()

            if not db.session.get(Universidad, universidad_id):
                universidad = Universidad(
                    id=universidad_id,
                    nombre=nombre,
                    sigla="N/A",
                    domicilio="Desconocido",
                    ciudad="Desconocida",
                    codigo_postal="0000",
                    telefono="000000",
                    email="desconocido@universidad.edu"
                )
                db.session.add(universidad)

        db.session.commit()
        print("✅ Importación completa.")

if __name__ == "__main__":
    importar_universidades(xml_path)
