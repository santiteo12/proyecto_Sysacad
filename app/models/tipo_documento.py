from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class TipoDocumento:
    dni: str
    libreta_civica: str
    libreta_enrolamiento = str
    pasaporte = str