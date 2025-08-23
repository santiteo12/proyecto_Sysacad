from app import db
from app.models.materia import Materia

class MateriaService:
    @staticmethod
    def crear_materia(materia: Materia):
        db.session.add(materia)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        return Materia.query.get(id)

    @staticmethod
    def buscar_todos() -> list[Materia]:
        return Materia.query.all()

    @staticmethod
    def actualizar_materia(id: int, nuevos_datos: Materia) -> Materia:
        materia = Materia.query.get(id)
        if not materia:
            return None
        materia.nombre = nuevos_datos.nombre
        materia.codigo = nuevos_datos.codigo
        materia.observacion = nuevos_datos.observacion
        db.session.commit()
        return materia

    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        materia = Materia.query.get(id)
        if not materia:
            return None
        db.session.delete(materia)
        db.session.commit()
        return None
