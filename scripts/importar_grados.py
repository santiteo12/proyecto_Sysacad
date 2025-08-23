import os
import sys
import xml.etree.ElementTree as ET

# Configurar contexto de Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.grado import Grado

def importar_grados(xml_path):
    print(f"📥 Importando grados desde: {xml_path}")

    # Leer con codificación Windows-1252
    tree = ET.parse(xml_path)
    root = tree.getroot()

    grados_xml = root.findall("_expxml")
    print(f"🔎 {len(grados_xml)} grados encontrados en el XML")

    count = 0
    for item in grados_xml:
        grado_id = int(item.find("grado").text)
        nombre = item.find("nombre").text.strip()

        if db.session.get(Grado, grado_id):
            print(f"⏩ Grado con ID {grado_id} ya existe.")
            continue

        grado = Grado(id=grado_id, nombre=nombre)
        db.session.add(grado)
        count += 1

    db.session.commit()
    print(f"✅ Importación completa. {count} grados nuevos agregados.")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        importar_grados("xml/grados.xml")
