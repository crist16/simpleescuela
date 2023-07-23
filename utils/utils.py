from datetime import datetime
import locale

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
