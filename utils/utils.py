from datetime import datetime
import locale
from email import encoders
from email.mime.base import MIMEBase

from docx2pdf import convert
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Establecer el idioma en español

meses = {
    'enero' : 1,
    'febrero' : 2,
    'marzo' : 3,
    'abril' : 4,
    'mayo' : 5,
    'junio' : 6,
    'julio' : 7,
    'agosto' : 8,
    'septiembre' : 9,
    'octubre' : 10,
    'noviembre' : 11,
    'diciembre' : 12,
}

def calcularEdad(Bday,Bmonth,Byear):
    locale.setlocale(locale.LC_TIME, 'es_ES')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - int(Byear)
    print(fecha_actual.month)
    if fecha_actual.month >= meses[Bmonth] and fecha_actual.day >= int(Bday):
        print(fecha_actual.year - int(Byear))
        return edad
    else:
        print(edad - 1)
        return edad -1


calcularEdad('4','julio','1994')




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

def enviar_correo_constanciaTrabajo(ruta_adjunto,file_name,destinatario, asunto, mensaje):
    # Configurar los detalles del servidor de correo
    remitente = "bolivariano.automated@gmail.com"
    contraseña = "rnguutslnoexyetr"
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587
    nombre_adjunto = file_name

    # Crear el objeto del mensaje
    correo = MIMEMultipart()
    correo["From"] = remitente
    correo["To"] = destinatario
    correo["Subject"] = asunto
    correo.add_header('Content-Disposition', 'attachment', filename='bud.gif')
    # Agregar el cuerpo del mensaje
    correo.attach(MIMEText(mensaje, "plain"))
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')

    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())

    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)

    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    correo.attach(adjunto_MIME)
    # Iniciar sesión en el servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    # Convertimos el objeto mensaje a texto
    texto = correo.as_string()

    # Enviar el correo electrónico
    servidor.sendmail(remitente,destinatario,texto)

    # Cerrar la conexión con el servidor SMTP
    servidor.quit()

