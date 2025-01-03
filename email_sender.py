import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
from utils import Colors

def get_ip():
    """Obtenemos la IP de la máquina local (o podemos poner una IP falsa)."""
    return "161.342.12.144"  

def get_current_time():
    """Obtenemos la hora actual del sistema."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def choose_email_body():
    """Permite al usuario elegir entre escribir un cuerpo o seleccionar una plantilla."""
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} ¿Quieres escribir tu propio cuerpo de correo o usar una plantilla?")
    print(f"{Colors.WARNING}[1]{Colors.ENDC} Escribir cuerpo del correo")
    print(f"{Colors.WARNING}[2]{Colors.ENDC} Elegir plantilla del correo")
    choice = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Elige una opción: ").strip()

    if choice == '1':
        # Opción 1: Escribir el cuerpo del correo manualmente
        body = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa el contenido del correo: ").strip()
    elif choice == '2':
        # Opción 2: Elegir una plantilla de correo
        templates_folder = './templates/email/'  # Asegúrate de que esta ruta sea correcta
        if not os.path.exists(templates_folder):
            print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} La carpeta de plantillas no existe.\n")
            body = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa el contenido del correo manualmente: ").strip()
        else:
            templates = [f for f in os.listdir(templates_folder) if f.endswith(('.txt', '.html'))]
            
            if not templates:
                print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se encontraron plantillas en la carpeta.\n")
                body = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa el contenido del correo manualmente: ").strip()
            else:
                print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Selecciona una plantilla:")
                for idx, template in enumerate(templates, 1):
                    print(f"{Colors.WARNING}[{idx}]{Colors.ENDC} {template}")
                
                template_choice = int(input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Elige una plantilla: ").strip()) - 1
                if 0 <= template_choice < len(templates):
                    # Cargar la plantilla seleccionada
                    with open(os.path.join(templates_folder, templates[template_choice]), 'r') as file:
                        body = file.read()
                    
                    # Solicitar la URL maliciosa y reemplazarla en el cuerpo de la plantilla
                    malicious_url = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa la URL maliciosa: ").strip()
                    body = body.replace("{{URL}}", malicious_url)  # Reemplazar el marcador de posición con la URL maliciosa
                    
                    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Plantilla seleccionada y cargada.\n")
                else:
                    print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Opción no válida, usando cuerpo personalizado por defecto.")
                    body = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa el contenido del correo: ").strip()
    else:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Opción no válida, usando cuerpo personalizado por defecto.")
        body = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa el contenido del correo: ").strip()
    
    return body

def phishing_by_email():
    """Función para el phishing por correo electrónico."""
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Phishing por correo electrónico seleccionado.\n")
    
    # Solicitar la dirección del objetivo
    email_address = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa la dirección de correo electrónico del objetivo: ").strip()
    subject = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa el asunto del correo: ").strip()
    
    # Solicitar las credenciales para el envío del correo
    sender_email = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa tu dirección de correo electrónico: ").strip()
    sender_password = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa tu contraseña de aplicación (o la contraseña de tu cuenta): ").strip()

    body = choose_email_body()  # Llamar a la función que permite elegir el cuerpo del correo

    # Reemplazar los marcadores de IP y hora en el cuerpo del correo
    ip = get_ip()
    current_time = get_current_time()
    body = body.replace("{{IP}}", ip).replace("{{TIME}}", current_time)

    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Preparando el correo electrónico de phishing...\n")

    try:
        # Configuración del servidor SMTP para enviar el correo (usando Gmail como ejemplo)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # Crear el objeto MIMEText para el cuerpo del mensaje
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email_address
        msg['Subject'] = subject
        
        # Si el cuerpo del correo tiene formato HTML
        if body.startswith("<html>") or body.startswith("<!DOCTYPE html>"):  # Se agregan más condiciones de HTML
            msg.attach(MIMEText(body, 'html'))  # Si es HTML, lo enviamos como tal
        else:
            msg.attach(MIMEText(body, 'plain'))  # Si no es HTML, lo enviamos como texto plano
        
        # Establecer conexión con el servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Seguridad para la conexión
        
        # Iniciar sesión en el servidor SMTP con las credenciales proporcionadas
        server.login(sender_email, sender_password)
        
        # Enviar el correo
        server.sendmail(sender_email, email_address, msg.as_string())
        server.quit()  # Cerrar la conexión
        
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Correo de phishing preparado y enviado a: {email_address}\n")
        
        # Confirmar el envío y preguntar si desea continuar o regresar
        choice = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Correo enviado correctamente. Presiona Enter para volver al menú principal o escribe 'r' para enviar otro correo: ").strip()
        if choice.lower() == 'r':
            phishing_by_email()  # Volver a ejecutar la función para enviar otro correo
        else:
            print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Volviendo al menú principal...\n")
    
    except Exception as e:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error al enviar el correo: {e}\n")
        choice = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ocurrió un error. Presiona Enter para intentar nuevamente o 'r' para regresar: ").strip()
        if choice.lower() == 'r':
            phishing_by_email()  # Volver a intentar el phishing
        else:
            print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Volviendo al menú principal...\n")
