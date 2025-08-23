from app import db

class Orientacion(db.Model):
    __tablename__ = 'orientaciones'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)

    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)

    especialidad = db.relationship('Especialidad')
    plan = db.relationship('Plan')
    materia = db.relationship('Materia')
