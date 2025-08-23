import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.pais import Pais

app = create_app()
xml_path = "xml/paises.xml"

def importar_paises(path: str):
    print(f"\n📥 Importando países desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} países encontrados en el XML")

    nuevos = 0

    with app.app_context():
        for r in registros:
            try:
                pais_id = int(r.find("pais").text)
                nombre = r.find("nombre").text.strip()

                if not db.session.get(Pais, pais_id):
                    pais = Pais(id=pais_id, nombre=nombre)
                    db.session.add(pais)
                    nuevos += 1
            except Exception as e:
                print(f"⚠️ Error procesando entrada: {ET.tostring(r, encoding='unicode')}\n{e}")
                db.session.rollback()

        db.session.commit()
        print(f"✅ Importación completa. {nuevos} países nuevos agregados.")

if __name__ == "__main__":
    importar_paises(xml_path)
