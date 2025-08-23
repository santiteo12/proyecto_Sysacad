import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia

app = create_app()
xml_path = "xml/orientaciones.xml"

def importar_orientaciones(path: str):
    print(f"\n📥 Importando orientaciones desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} orientaciones encontradas en el XML")

    with app.app_context():
        id_autogenerado = db.session.query(Orientacion).count() + 1

        for r in registros:
            try:
                nombre = r.find("nombre").text.strip()
                especialidad_id = int(r.find("especialidad").text)
                plan_id = int(r.find("plan").text)

                especialidad = db.session.get(Especialidad, especialidad_id)
                plan = db.session.get(Plan, plan_id)
                materia = db.session.query(Materia).first()

                if not all([especialidad, plan, materia]):
                    print(f"⚠️ Datos faltantes para orientación '{nombre}', se omite.")
                    continue

                orientacion = Orientacion(
                    id=id_autogenerado,
                    nombre=nombre,
                    especialidad_id=especialidad_id,
                    plan_id=plan_id,
                    materia_id=materia.id
                )

                db.session.add(orientacion)
                id_autogenerado += 1

            except Exception as e:
                db.session.rollback()
                print(f"❌ Error procesando entrada: {e}")

        db.session.commit()
        print("✅ Importación completa.")

if __name__ == "__main__":
    importar_orientaciones(xml_path)
