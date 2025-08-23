import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.plan import Plan

app = create_app()
xml_path = "xml/planes.xml"

def importar_planes(path: str):
    print(f"\n📥 Importando planes desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} planes encontrados en el XML")

    with app.app_context():
        for r in registros:
            try:
                plan_id = int(r.find("plan").text)
                nombre = r.find("nombre").text.strip() if r.find("nombre") is not None and r.find("nombre").text else f"Plan {plan_id}"

                if not db.session.get(Plan, plan_id):
                    plan = Plan(
                        id=plan_id,
                        nombre=nombre,
                        fecha_inicio="2000-01-01",  # Valor genérico
                        fecha_fin="2099-12-31",     # Valor genérico
                        observacion="Sin observaciones"
                    )
                    db.session.add(plan)
            except Exception as e:
                print(f"⚠️ Entrada inválida, se omite: {ET.tostring(r, encoding='unicode')}\n  ⛔ {e}")

        db.session.commit()
        print("✅ Importación completa.")

if __name__ == "__main__":
    importar_planes(xml_path)
