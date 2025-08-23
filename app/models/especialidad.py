from app import db
from app.models.tipo_especialidad import TipoEspecialidad

class Especialidad(db.Model):
    __tablename__ = 'especialidades'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    letra = db.Column(db.String(10), nullable=False)
    observacion = db.Column(db.String(200))
    
    tipo_especialidad_id = db.Column(db.Integer, db.ForeignKey('tipos_especialidad.id'), nullable=False)
    tipo_especialidad = db.relationship('TipoEspecialidad', backref='especialidades')
