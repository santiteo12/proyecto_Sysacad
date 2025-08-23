import os
import sys
import xml.etree.ElementTree as ET

# Contexto Flask
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ["FLASK_CONTEXT"] = "development"

from app import create_app, db
from app.models.localidad import Localidad
from app.models.provincia import Provincia

app = create_app()
xml_path = "xml/localidades.xml"

def importar_localidades(path: str):
    print(f"\n📥 Importando localidades desde: {path}")
    tree = ET.parse(path)
    root = tree.getroot()
    registros = root.findall(".//_exportar")
    print(f"🔎 {len(registros)} localidades encontradas en el XML")

    nuevas = 0
    with app.app_context():
        for r in registros:
            try:
                localidad_id = int(r.find("codigo").text)
                nombre = r.find("ciudad").text.strip()
                provincia_nombre = r.find("provincia").text.strip()
                provincia = db.session.query(Provincia).filter_by(nombre=provincia_nombre).first()

                if not provincia:
                    print(f"⚠️ Provincia no encontrada: {provincia_nombre} — Se omite localidad {nombre}")
                    continue

                if not db.session.get(Localidad, localidad_id):
                    localidad = Localidad(
                        id=localidad_id,
                        nombre=nombre,
                        codigo_postal=None,  # No está en el XML
                        provincia_id=provincia.id
                    )
                    db.session.add(localidad)
                    nuevas += 1

            except Exception as e:
                print(f"⚠️ Error procesando entrada: {ET.tostring(r, encoding='unicode')}\n   ↳ Error: {e}")

        db.session.commit()
        print(f"✅ Importación completa. {nuevas} localidades nuevas agregadas.")

if __name__ == "__main__":
    importar_localidades(xml_path)
