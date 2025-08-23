from app import db

class TipoEspecialidad(db.Model):
    __tablename__ = 'tipos_especialidad'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    nivel = db.Column(db.String(50), nullable=False)
