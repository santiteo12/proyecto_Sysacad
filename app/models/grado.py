from app import db

class Grado(db.Model):
    __tablename__ = 'grados'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
