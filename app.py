from app import create_app
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Crear app
app = create_app()

# Empujar el contexto (opcional, según si lo necesitás para inicializar algo antes de correr)
app.app_context().push()

# Definir rutas
@app.route('/')
def index():
    return "Hola mundo"

# Método tradicional para ejecutar
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
