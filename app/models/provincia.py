from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Provincia(db.Model):
    __tablename__ = 'provincias'

    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    pais_id: int = db.Column(db.Integer, db.ForeignKey('paises.pais'), nullable=False)
