Autores :santaigo Garcia

### descripcion del proyecto ###

El proyecto SYSACAD es un sistema académico desarrollado con Python y Flask utilizando una base de datos de PostgreSQL, cuyo objetivo es centralizar y automatizar la gestión de la información académica. La aplicación permite administrar alumnos, planes de estudio, materias, facultades y autoridades, garantizando integridad de datos y facilitando el acceso a la información. Su diseño modular, basado en buenas prácticas de desarrollo y un modelo relacional, lo convierte en una solución escalable y adaptable a las necesidades de instituciones educativas.


### para ejecutarlo ###
Crear el entorno virtual
Ejecutar en la raíz del proyecto:

python -m venv venv

Activar el entorno virtual
En Windows:
venv\Scripts\activate

En macOS / Linux:
source venv/bin/activate

Instalar dependencias
Con el entorno virtual activo, instalar las dependencias necesarias:
pip install -r requirements.txt

luego para iniciar la aplicacion y generar un servidor de prueba como local host :
python app.py

Limpiar tablas existentes
Para eliminar las tablas previas (si las hay), ejecutar:
python scripts/reset_tablas.py

Importar todos los datos
Ejecutar el importador general de datos XML:
python scripts/importar_todo.py
