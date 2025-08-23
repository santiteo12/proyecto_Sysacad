
from app import db

class Universidad(db.Model):
    __tablename__ = 'universidades'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(20), nullable=False)
    domicilio = db.Column(db.String(100))
    ciudad = db.Column(db.String(100))
    codigo_postal = db.Column(db.String(10))
    telefono = db.Column(db.String(30))
    email = db.Column(db.String(100))


