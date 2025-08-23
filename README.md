⚙️ Crear el entorno virtual
Ejecutar en la raíz del proyecto:

python -m venv venv

▶️ Activar el entorno virtual
En Windows:
venv\Scripts\activate

En macOS / Linux:
source venv/bin/activate

Una vez activado, el prompt mostrará algo como:
(venv) C:\ruta\al\proyecto>

📦 Instalar dependencias
Con el entorno virtual activo, instalar las dependencias necesarias:
pip install -r requirements.txt

🚀 Probar el script de importación
Si querés probar el proceso completo de importación de datos desde los XML, seguí estos pasos:

🧹 Limpiar tablas existentes
Para eliminar las tablas previas (si las hay), ejecutar:
python scripts/reset_tablas.py

📥 Importar todos los datos
Ejecutar el importador general de datos XML:
python scripts/importar_todo.py
