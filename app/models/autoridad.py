from dataclasses import dataclass
from app.models.cargo import Cargo
from app import db

@dataclass(init=False, repr=True, eq=True)
#TODO añadir id a la base de datos
class Autoridad():
    id: str = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    cargo_id: int = db.Column(db.Integer, db.ForeignKey('cargo.id'), nullable=False)
    telefono: int = db.Column(db.String(20), nullable=True)
    email: str = db.Column(db.String(100), nullable=True)