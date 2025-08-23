from app import db
from app.models.universidad import Universidad

class UniversidadService:
    @staticmethod
    def crear_universidad(universidad: Universidad):
        db.session.add(universidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int) -> Universidad:
        return Universidad.query.get(id)

    @staticmethod
    def buscar_todos() -> list[Universidad]:
        return Universidad.query.all()

    @staticmethod
    def actualizar_universidad(id: int, nuevos_datos: Universidad) -> Universidad:
        universidad = Universidad.query.get(id)
        if not universidad:
            return None
        universidad.nombre = nuevos_datos.nombre
        universidad.sigla = nuevos_datos.sigla
        universidad.domicilio = nuevos_datos.domicilio
        universidad.ciudad = nuevos_datos.ciudad
        universidad.codigo_postal = nuevos_datos.codigo_postal
        universidad.telefono = nuevos_datos.telefono
        universidad.email = nuevos_datos.email
        db.session.commit()
        return universidad

    @staticmethod
    def borrar_por_id(id: int) -> Universidad:
        universidad = Universidad.query.get(id)
        if not universidad:
            return None
        db.session.delete(universidad)
        db.session.commit()
        return None
