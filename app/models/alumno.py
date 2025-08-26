from dataclasses import dataclass
from app import db
from enum import Enum
from datetime import date

class TipoDocumento(Enum):
    dni = "DNI"
    libreta_civica = "Libreta Cívica"
    libreta_enrolamiento = "Libreta de Enrolamiento"
    pasaporte = "Pasaporte"

class Sexo(Enum):
    masculino = "M"
    femenino = "F"
    otro = "O"

@dataclass(init=False, repr=True, eq=True)
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    apellido: str = db.Column(db.String(100), nullable=False)
    nombre: str = db.Column(db.String(100), nullable=False)
    nro_documento: str = db.Column(db.String(20), nullable=False, unique=True)
    tipo_documento: int = db.Column(db.Enum(TipoDocumento), nullable=False)
    fecha_nacimiento: date = db.Column(db.Date, nullable=False)
    sexo: str = db.Column(db.Enum(Sexo), nullable=False)
    nro_legajo: int = db.Column(db.Integer, nullable=False, unique=True)
    fecha_ingreso: date = db.Column(db.Date, nullable=False)
#TODO añadir para agregar alumno
    def nuevo_alumno():