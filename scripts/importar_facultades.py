import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.facultad import Facultad

app = create_app()
xml_path = "xml/facultades.xml"

def importar_facultades(path: str):
    print(f"\n📥 Importando facultades desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} facultades encontradas en el XML")

    with app.app_context():
        for r in registros:
            facultad_id = int(r.find("facultad").text)
            nombre = r.find("nombre").text.strip()

            if not db.session.get(Facultad, facultad_id):
                facultad = Facultad(
                    id=facultad_id,
                    nombre=nombre,
                    abreviatura="N/A",
                    directorio="N/A",
                    sigla="N/A",
                    codigo_postal=None,
                    ciudad=None,
                    domicilio=None,
                    telefono=None,
                    contacto=None,
                    email="desconocido@utn.edu.ar"
                )
                db.session.add(facultad)

        db.session.commit()
        print("✅ Importación completa.")

if __name__ == "__main__":
    importar_facultades(xml_path)
