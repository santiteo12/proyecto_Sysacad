from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Localidad(db.Model):
    __tablename__ = 'localidades'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    codigo_postal: str = db.Column(db.String(20), nullable=True)
    provincia_id: int = db.Column(db.Integer, db.ForeignKey('provincias.id'), nullable=False)
