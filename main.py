import tempfile
from datetime import datetime
import os
import random
import zipfile
from docxtpl import DocxTemplate

from flask import Flask, request, send_file

from utils.utils import getFullActualDate, ConvertToPdf

app = Flask(__name__)

@app.route("/")
def Home():
    return "Mi aplicacion flask acaba de cambiar again"

#Constancias

@app.route('/constancia_de_trabajo', methods=['POST'])
def Constancia_de_trabajo():

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
    print(context)
    # Crear un archivo temporal
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as temp_file:
        archivo_temporal = temp_file.name

        # Cargar la plantilla de documento
        doc = DocxTemplate(f'inputs/templates/constancia_trabajo.docx')
        doc.render(context)

        doc.save(f"outputs/{request.form.get('Nombres')}.docx")

    #return f"http://localhost:4000/constancia_de_trabajo"
        # Retornar el archivo temporal como descarga adjunta

    return send_file(path_or_file=f"outputs/{request.form.get('Nombres')}.docx",as_attachment=True)




@app.route('/constancia_de_estudio',methods =['POST'])
def Constancia_de_estudio():
    return 'received'


@app.route('/constancia_de_prosecucion',methods = ['POST'])
def Constancia_de_prosecucion():
    lista_de_archivos = []
    solicitud = request.get_json()
    fecha_actual = getFullActualDate()
    fecha = datetime.now()
    fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S")
    fecha_mes = int(fecha_str.split('-')[1])
    if fecha_mes < 8:

        periodo_escolar = f"{fecha_actual['year']-1}-{fecha_actual['year']}"

    else:
        periodo_escolar = f"{fecha_actual['year']}-{fecha_actual['year']+1}"
    folder = random.randint(0,10000)
    # Ruta de la carpeta que deseas crear
    carpeta = f'outputs/{folder}'

    # Verificar si la carpeta no existe
    if not os.path.exists(carpeta):
        # Crear la carpeta
        os.makedirs(carpeta)
        print(f'Carpeta "{carpeta}" creada exitosamente.')
    else:
        print(f'La carpeta "{carpeta}" ya existe.')
    for item in solicitud:
        context = {
            "nombre_estudiante" : item['nombre'],
            "cedula_estudiante": item['cedula'],
            "lugar_nacimiento": item['lugarNacimiento'],
            "fecha_nacimiento": item['fechaNacimiento'],
            "literal": item['literal'],
            "periodo_escolar": periodo_escolar,
            "dia": fecha_actual['dia'],
            "mes": fecha_actual['mes'],
            "year": fecha_actual['year'],

        }

        doc = DocxTemplate(f'inputs/templates/prosecucion.docx')
        doc.render(context)

        doc.save(f"outputs/{folder}/{item['nombre']}.docx")
        lista_de_archivos.append(f"outputs/{folder}/{item['nombre']}.docx")
    archivo_zip = f'outputs/{folder}.zip'

    # Crear un objeto ZipFile y abrirlo en modo escritura
    with zipfile.ZipFile(archivo_zip, 'w') as zipf:
        # Agregar los archivos al archivo ZIP
        for archivo in lista_de_archivos:
            zipf.write(archivo)



    print(archivo_zip)
    return send_file(archivo_zip,as_attachment=True)


if __name__ == "__main__":
    app.run(port=4000,debug=True)