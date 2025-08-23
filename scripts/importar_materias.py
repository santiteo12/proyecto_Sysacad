import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.materia import Materia

app = create_app()
xml_path = "xml/materias.xml"

def importar_materias(path: str):
    print(f"\n📥 Importando materias desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} materias encontradas en el XML")

    with app.app_context():
        for r in registros:
            materia_id = int(r.find("materia").text)
            nombre = r.find("nombre").text.strip() if r.find("nombre") is not None else "Materia sin nombre"
            codigo = str(materia_id)
            observacion = "Importado desde XML"

            if not db.session.get(Materia, materia_id):
                materia = Materia(
                    id=materia_id,
                    nombre=nombre,
                    codigo=codigo,
                    observacion=observacion
                )
                db.session.add(materia)

        db.session.commit()
        print("✅ Importación completa.")

if __name__ == "__main__":
    importar_materias(xml_path)
