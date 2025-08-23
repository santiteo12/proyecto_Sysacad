from app import db

class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    observacion = db.Column(db.String(200))
