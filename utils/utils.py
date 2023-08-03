from datetime import datetime
import locale
from docx2pdf import convert
# Establecer el idioma en español


def getFullActualDate():
    locale.setlocale(locale.LC_TIME, 'es_ES')
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    # Obtener el día, mes y año
    dia = fecha_actual.day
    mes = fecha_actual.strftime("%B")  # El mes en formato completo
    year = fecha_actual.year
    fecha_actual = {
        'dia' : dia,
        'mes' : mes,
        'year' : year
    }
    return fecha_actual


def ConvertToPdf(ruta_entrada , ruta_salida):    # Ruta del archivo DOCX de entrada y ruta de salida para el PDF

    convert(ruta_entrada, ruta_salida)