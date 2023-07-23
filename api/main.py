import json
import os
from docxtpl import DocxTemplate

from flask import Flask, request

from utils.utils import getFullActualDate

app = Flask(__name__)

@app.route("/")
def Home():
    return "Mi aplicacion flask acaba de cambiar"

#Constancias

@app.route('/constancia_de_trabajo', methods=['GET'])
def Constancia_de_trabajo():
    fecha_actual = getFullActualDate()
    """
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
        doc = DocxTemplate(r"inputs/templates/constancia_trabajo.docx")
        doc.render(context)
        doc.save(f"outputs/{request.form.get('Nombres')}.docx")
    """
    return 'received'

@app.route('/constancia_de_estudio',methods =['POST'])
def Constancia_de_estudio():
    return 'received'

if __name__ == "__main__":
    app.run(port=4000,debug=True)