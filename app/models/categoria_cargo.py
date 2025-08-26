from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo:
    #TODO añadir codigo para guardar en la base de datos
    nombre: str
    
    