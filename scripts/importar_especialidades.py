import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad

app = create_app()
xml_path = "xml/especialidades.xml"

def importar_especialidades(path: str):
    print(f"\n📥 Importando especialidades desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_expxml")
    print(f"🔎 {len(registros)} especialidades encontradas en el XML")

    nuevas = 0
    omitidas = 0

    with app.app_context():
        tipo = db.session.get(TipoEspecialidad, 1)
        if not tipo:
            tipo = TipoEspecialidad(id=1, nombre="Genérico", nivel="Genérico")
            db.session.add(tipo)
            db.session.commit()
            print("🆕 TipoEspecialidad genérico creado.")

        for r in registros:
            try:
                especialidad_id = int(r.find("especialidad").text)
                nombre = r.find("nombre").text.strip()

                if db.session.get(Especialidad, especialidad_id):
                    omitidas += 1
                    continue

                especialidad = Especialidad(
                    id=especialidad_id,
                    nombre=nombre,
                    letra="N/A",
                    observacion=None,
                    tipo_especialidad_id=tipo.id
                )
                db.session.add(especialidad)
                nuevas += 1
            except Exception as e:
                print(f"⚠️ Error procesando entrada: {ET.tostring(r, encoding='unicode')} -> {e}")
                db.session.rollback()

        db.session.commit()
        print(f"✅ Importación completa. {nuevas} especialidades nuevas agregadas.")
        print(f"ℹ️ {omitidas} especialidades ya existían y fueron omitidas.")

if __name__ == "__main__":
    importar_especialidades(xml_path)
