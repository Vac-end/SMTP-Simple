import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# Configuración de credenciales de cPanel
EMAIL_USER = os.getenv("EMAIL_USER")       # Reemplaza con tu correo de cPanel
EMAIL_PASS = os.getenv("EMAIL_PASS")                # Reemplaza con la contraseña de tu correo de cPanel
SMTP_SERVER = os.getenv("SMTP_SERVER")           # Reemplaza con el servidor SMTP de tu cPanel
SMTP_PORT = os.getenv("SMTP_PORT")                               # Puerto SMTP seguro para cPanel

# Información del correo
DESTINATARIOS = ["Correo1@example.com", "Correo2@example.com"]       # Reemplaza con el correo del destinatario
ASUNTO = "Asunto"                   # Reemplaza con el asunto del correo
TEXTO = " "        # Reemplaza con el texto del correo
HTML_CONTENT = """
<html>
  <body>
    <h1>Este es un correo HTML</h1>
    <p>Este es el contenido del correo en formato HTML.</p>
  </body>
</html>
"""

# Crear el mensaje
def crear_mensaje(destinatarios, asunto, texto, html_content):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = ", ".join(destinatarios)  # Convertir lista a cadena separada por comas
    msg['Subject'] = asunto
    msg.attach(MIMEText(texto, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))
    return msg

# Enviar el correo usando smtplib
def enviar_correo(destinatarios):
    # Asegurarse de que 'destinatarios' sea una lista, incluso si es un solo correo
    if isinstance(destinatarios, str):
        destinatarios = [destinatarios]  # Convertir a lista si es una cadena única

    msg = crear_mensaje(destinatarios, ASUNTO, TEXTO, HTML_CONTENT)

    # Establecer conexión segura con el servidor SMTP
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_USER, EMAIL_PASS)  # Autenticación
        server.sendmail(EMAIL_USER, destinatarios, msg.as_string())
        print(f"Correo enviado exitosamente a: {', '.join(destinatarios)}")

# Ejecutar la función de envío al iniciar el script
if __name__ == "__main__":
    enviar_correo(DESTINATARIOS)

