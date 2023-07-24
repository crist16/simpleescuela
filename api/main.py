import json
import os
import tempfile
from docxtpl import DocxTemplate

from flask import Flask, request, send_file

from utils.utils import getFullActualDate

app = Flask(__name__)

@app.route("/")
def Home():
    return "Mi aplicacion flask acaba de cambiar again"

#Constancias

@app.route('/constancia_de_trabajo', methods=['POST'])
def Constancia_de_trabajo():
    print("sfddfsd")
    fecha_actual = getFullActualDate()

    context = {
    'Nombres' : request.form.get('Nombres'),
    'Apellidos' : request.form.get('Apellidos'),
    'Cedula' : request.form.get('Cedula'),
    'Cargo' : request.form.get('Cargo'),
    'fecha_ingreso' : request.form.get('Fecha_ingreso'),
    'dia' : fecha_actual['dia'],
    'mes' : fecha_actual['mes'],
    'year' : fecha_actual['year'] ,
    }
    # Crear un archivo temporal
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as temp_file:
        archivo_temporal = temp_file.name

        # Cargar la plantilla de documento
        doc = DocxTemplate(f'inputs/templates/constancia_trabajo.docx')
        doc.render(context)
        # Realizar las modificaciones necesarias en la plantilla
        # Puedes utilizar doc.render(context) para pasarle datos dinámicos a la plantilla
        # Guardar el documento generado en el archivo temporal
        doc.save(archivo_temporal)
        ruta_absoluta = os.path.abspath(archivo_temporal)

        # Retornar el archivo temporal como descarga adjunta
    return ruta_absoluta




@app.route('/constancia_de_estudio',methods =['POST'])
def Constancia_de_estudio():
    return 'received'

if __name__ == "__main__":
    app.run(port=4000,debug=True)