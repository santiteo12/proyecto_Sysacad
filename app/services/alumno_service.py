import datetime
from io import BytesIO
import os
from pathlib import Path

from flask import render_template, current_app, url_for
from weasyprint import HTML
from python_odt_template import ODTTemplate
from python_odt_template.jinja import get_odt_renderer
from docxtpl import DocxTemplate
import jinja2

from app.models import Alumno
from app.repositories import AlumnoRepository

class AlumnoService:

    @staticmethod
    def crear(alumno):
        AlumnoRepository.crear(alumno)

    @staticmethod
    def buscar_por_id(id: int) -> Alumno:        
        return AlumnoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Alumno]:
        return AlumnoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, alumno: Alumno) -> Alumno:
        alumno_existente = AlumnoRepository.buscar_por_id(id)
        if not alumno_existente:
            return None
        alumno_existente.nombre = alumno.nombre
        alumno_existente.apellido = alumno.apellido
        alumno_existente.nrodocumento = alumno.nrodocumento
        alumno_existente.tipo_documento = alumno.tipo_documento
        alumno_existente.fecha_nacimiento = alumno.fecha_nacimiento
        alumno_existente.sexo = alumno.sexo
        alumno_existente.nro_legajo = alumno.nro_legajo
        alumno_existente.fecha_ingreso = alumno.fecha_ingreso
        return alumno_existente
        
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return AlumnoRepository.borrar_por_id(id)
    
    @staticmethod
    def generar_certificado_alumno_regular(id: int):
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None
        
        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        
        universidad = facultad.universidad
        html_string = render_template('certificado/certificado_pdf.html', alumno=alumno,
                                    facultad=facultad,
                                    especialidad=especialidad,
                                    universidad=universidad,
                                    fecha=fecha_str)
        base_url = url_for('static', filename='', _external=True)
        bytes_data = HTML(string=html_string, base_url=base_url).write_pdf()
        pdf_io = BytesIO(bytes_data)
        return pdf_io

    @staticmethod
    def generar_certificado_alumno_regular_odt(id: int):
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None

        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        
        odt_renderer = get_odt_renderer(media_path=url_for('static', filename='media'))
        path_template = os.path.join(current_app.root_path, 'templates', 'certificado', 'certificado_plantilla.odt')
        
        
        odt_io = BytesIO()
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
            temp_path = temp_file.name

        with ODTTemplate(path_template) as template:
            odt_renderer.render( template,
                context={
                        "alumno":alumno, 
                        "facultad": facultad, 
                        "especialidad": especialidad, 
                        "universidad": universidad, 
                        "fecha": fecha_str
                        }
            )
            template.pack(temp_path)
            with open(temp_path, 'rb') as f:
                odt_io.write(f.read())
            
        os.unlink(temp_path)
        odt_io.seek(0)
        return odt_io
    
    @staticmethod
    def generar_certificado_alumno_regular_docx(id: int):
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None
        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        path_template = os.path.join(current_app.root_path, 'templates', 'certificado', 'certificado_plantilla.docx')
        doc = DocxTemplate(path_template)
        
        docx_io = BytesIO()
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.odt', delete=False) as temp_file:
            temp_path = temp_file.name

        context={
                "alumno":alumno, 
                "facultad": facultad, 
                "especialidad": especialidad, 
                "universidad": universidad, 
                "fecha": fecha_str
                }
        jinja_env = jinja2.Environment()
    
        doc.render(context, jinja_env)
        doc.save(temp_path)
        with open(temp_path, 'rb') as f:
                docx_io.write(f.read())
            
        os.unlink(temp_path)
        docx_io.seek(0)
        return docx_io