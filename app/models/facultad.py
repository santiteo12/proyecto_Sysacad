from app import db

class Facultad(db.Model):
    __tablename__ = 'facultades'
#TODO añadir id a la base de datos 
    id: int  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    abreviatura = db.Column(db.String(10), nullable=False)
    directorio = db.Column(db.String(100), nullable=False)
    sigla = db.Column(db.String(10), nullable=False)
    codigo_postal = db.Column(db.String(10))
    ciudad = db.Column(db.String(50))
    domicilio = db.Column(db.String(100))
    telefono = db.Column(db.String(20))
    contacto = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False)
