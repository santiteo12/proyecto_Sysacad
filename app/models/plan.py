from app import db

class Plan(db.Model):
    __tablename__ = 'planes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_inicio = db.Column(db.String(50), nullable=False)
    fecha_fin = db.Column(db.String(50), nullable=False)
    observacion = db.Column(db.String(200))
