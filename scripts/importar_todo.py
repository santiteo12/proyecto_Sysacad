import os
import sys
import runpy

# Ruta a la carpeta de scripts
SCRIPTS_DIR = os.path.dirname(__file__)

# Scripts a ejecutar en orden
scripts = [
    "importar_paises.py",
    "importar_provincias.py",
    "importar_localidades.py",
    "importar_grados.py",
    "importar_universidades.py",
    "importar_facultades.py",
    "importar_especialidades.py",
    "importar_planes.py",
    "importar_materias.py",
    "importar_orientaciones.py"
]

print("📦 INICIANDO IMPORTACIÓN TOTAL...\n")

for script in scripts:
    print(f"▶ Ejecutando: {script}...")
    script_path = os.path.join(SCRIPTS_DIR, script)

    try:
        runpy.run_path(script_path, run_name="__main__")
    except Exception as e:
        print(f"🛑 Error en: {script} — Se detiene la ejecución.")
        print(f"   ↳ {e}")
        sys.exit(1)

print("\n✅ Todos los scripts fueron ejecutados correctamente.")
