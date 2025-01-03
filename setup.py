import os
import subprocess
import sys

# Colores para la terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Nuevo ASCII art
ASCII_ART = f"""
{Colors.BLUE}
        _     _     _              _           ____       _                   
  _ __ | |__ (_)___| |_ ___   ___ | |         / ___|  ___| |_ _   _ _ __  
 | '_ \| '_ \| / __| __/ _ \ / _ \| |  _____  \___ \ / _ \ __| | | | '_ \ 
 | |_) | | | | \__ \ || (_) | (_) | | |_____|  ___) |  __/ |_| |_| | |_) |
 | .__/|_| |_|_|___/\__\___/ \___/|_|         |____/ \___|\__|\__,_| .__/ 
 |_|                                                               |_|    
{Colors.GREEN}
                                                            by saimonch16
{Colors.ENDC}
"""

def clear_terminal():
    """Limpia la terminal dependiendo del sistema operativo."""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Unix/MacOS
        os.system('clear')

def check_ngrok_token():
    """Verifica si ngrok ya tiene un token de autenticación almacenado."""
    config_file_path = os.path.expanduser('~/.ngrok2/ngrok.yml')
    
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            content = f.read()
            if 'authtoken:' in content:
                return True
    return False

def setup_ngrok():
    """Configura ngrok si no está autenticado y actualiza la configuración."""
    try:
        # Verificar si ngrok está instalado
        subprocess.run(["ngrok", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Ngrok no está instalado. Por favor, instálalo antes de continuar.\n")
        return
    
    if check_ngrok_token():
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Ngrok ya está autenticado.\n")
        # Intentar actualizar el archivo de configuración
        try:
            subprocess.run(["ngrok", "config", "upgrade"], check=True)
            print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Archivo de configuración de ngrok actualizado correctamente.\n")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error al actualizar el archivo de configuración: {e}\n")
        return

    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} No se encontró un token de autenticación para ngrok.\n")
    
    has_account = input(f"{Colors.WARNING}[INFO]{Colors.ENDC} ¿Ya tienes una cuenta en ngrok? (s/n): ").strip().lower()

    if has_account == 's':
        print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Antes de continuar, por favor, visita esta URL para visualizar tu token de autenticación: https://dashboard.ngrok.com/get-started/your-authtoken")
        input(f"{Colors.WARNING}[INFO]{Colors.ENDC} Pulsa Enter una vez que hayas visualizado tu token...\n")
        token = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Ingresa tu token de autenticación de ngrok: ").strip()
        save_ngrok_token(token)
    else:
        print(f"{Colors.WARNING}[INFO]{Colors.ENDC} No tienes cuenta. Crea una cuenta en: https://ngrok.com\n")
        input(f"{Colors.WARNING}[INFO]{Colors.ENDC} Pulsa Enter una vez que te hayas registrado o si ya tienes una cuenta para continuar...\n")
        setup_ngrok()
    
    # Actualizar el archivo de configuración
    try:
        subprocess.run(["ngrok", "config", "upgrade"], check=True)
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Archivo de configuración de ngrok actualizado correctamente.\n")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error al actualizar el archivo de configuración: {e}\n")

def save_ngrok_token(token):
    """Guarda el token de autenticación en el archivo de configuración de ngrok."""
    config_file_path = os.path.expanduser('~/.ngrok2/ngrok.yml')
    
    if not os.path.exists(os.path.dirname(config_file_path)):
        os.makedirs(os.path.dirname(config_file_path))

    with open(config_file_path, 'w') as f:
        f.write(f'authtoken: {token}\n')
    
    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Token guardado correctamente en {config_file_path}.\n")

def check_dependencies(requirements_file):
    """Verifica las dependencias en requirements.txt y muestra el estado."""
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Verificando dependencias...\n")
    pip_executable = os.path.join('venv', 'bin', 'pip') if os.name != 'nt' else os.path.join('venv', 'Scripts', 'pip')

    try:
        installed_packages = subprocess.check_output([pip_executable, 'freeze'], text=True).splitlines()
        installed = {pkg.split('==')[0].lower() for pkg in installed_packages}
    except FileNotFoundError:
        installed = set()

    with open(requirements_file, 'r') as f:
        requirements = [line.strip().split('==')[0] for line in f if line.strip()]
    
    for pkg in requirements:
        if pkg.lower() in installed:
            print(f"{Colors.GREEN}✓ {pkg}{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}✗ {pkg}{Colors.ENDC}")
    print()

def create_virtualenv():
    """Crea un entorno virtual."""
    if not os.path.exists('venv'):
        print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Creando entorno virtual...\n")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'])
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Entorno virtual creado.\n")
    else:
        print(f"{Colors.WARNING}[INFO]{Colors.ENDC} El entorno virtual ya existe.\n")

def install_requirements():
    """Instala las dependencias desde requirements.txt."""
    if not os.path.exists('requirements.txt'):
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se encontró requirements.txt. Por favor, crea uno antes de continuar.\n")
        return

    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Instalando dependencias...\n")
    pip_executable = os.path.join('venv', 'bin', 'pip') if os.name != 'nt' else os.path.join('venv', 'Scripts', 'pip')
    subprocess.run([pip_executable, 'install', '-r', 'requirements.txt', '-q'])  # Reducción de salida con '-q'
    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Dependencias instaladas.\n")

def install_ngrok():
    """Instala ngrok usando apt si no está instalado."""
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Verificando si ngrok está instalado...\n")
    try:
        result = subprocess.run(["ngrok", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Ngrok ya está instalado.\n")
    except FileNotFoundError:
        print(f"{Colors.FAIL}[INFO]{Colors.ENDC} Ngrok no está instalado. Procediendo con la instalación...\n")
        
        # Instalación de ngrok usando apt
        try:
            subprocess.run("curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null", shell=True, check=True)
            subprocess.run("echo \"deb https://ngrok-agent.s3.amazonaws.com buster main\" | sudo tee /etc/apt/sources.list.d/ngrok.list", shell=True, check=True)
            subprocess.run("sudo apt update", shell=True, check=True)
            subprocess.run("sudo apt install ngrok", shell=True, check=True)
            print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Ngrok instalado correctamente.\n")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Error al instalar ngrok: {e}\n")

def add_to_path(path):
    """Agrega un directorio al PATH del sistema y le indica al usuario qué comando ejecutar para actualizar la terminal."""
    shell = os.environ.get('SHELL', '').lower()
    user_home = os.path.expanduser("~")

    if 'bash' in shell:
        rc_file = os.path.join(user_home, '.bashrc')
        command = f'export PATH="$PATH:{path}"'
    elif 'zsh' in shell:
        rc_file = os.path.join(user_home, '.zshrc')
        command = f'export PATH="$PATH:{path}"'
    else:
        print(f"{Colors.WARNING}[INFO]{Colors.ENDC} No se pudo identificar el shell, no se ha agregado al PATH.\n")
        return

    # Agregar al archivo de configuración del shell
    try:
        with open(rc_file, 'a') as file:
            file.write(f"\n# Agregado por el script para ngrok\n{command}\n")
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Se ha agregado {path} al {rc_file}.\n")
    except Exception as e:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se pudo actualizar el archivo {rc_file}: {e}\n")

    # Indicar al usuario que ejecute el comando para actualizar el PATH en la terminal
    print(f"{Colors.WARNING}[INFO]{Colors.ENDC} Para actualizar el PATH en tu terminal, ejecuta el siguiente comando:")
    print(f"{Colors.GREEN}[TIP]{Colors.ENDC} source {rc_file} (o el comando correspondiente según tu shell)\n")

def main():
    clear_terminal()  # Limpia la terminal antes de mostrar cualquier mensaje
    print(ASCII_ART)
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Iniciando configuración del entorno...\n")
    
    create_virtualenv()

    requirements_file = 'requirements.txt'
    if os.path.exists(requirements_file):
        check_dependencies(requirements_file)
        install_requirements()
    else:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} No se encontró el archivo {requirements_file}. Por favor, asegúrate de crearlo antes de continuar.\n")

    install_ngrok()

    ngrok_bin_path = os.path.expanduser("~/.local/bin")
    add_to_path(ngrok_bin_path)

    setup_ngrok()

    if os.name != 'nt':  # Linux/Unix/MacOS
        activate_cmd = "source venv/bin/activate"
    else:  # Windows
        activate_cmd = ".\\venv\\Scripts\\activate"

    print(f"{Colors.WARNING}[INFO]{Colors.ENDC} El entorno virtual está listo.")
    print(f"{Colors.GREEN}[TIP]{Colors.ENDC} Usa '{activate_cmd}' para activarlo manualmente.")
    print(f"{Colors.GREEN}[TIP]{Colors.ENDC} Una vez finalizado, desactívalo con: deactivate\n")
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Configuración completa.\n\n\n")

    print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Para usar la herramienta, ejecuta: python3 main.py\n")

if __name__ == "__main__":
    main()
