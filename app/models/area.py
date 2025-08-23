from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Area(db.Model):
    __tablename__ = 'areas'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(50), nullable=False)