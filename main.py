import os
from email_sender import phishing_by_email
from malicious_url import phishing_by_url
from utils import clear_terminal, Colors, ASCII_ART_PHISHING

def display_menu():
    """Función para mostrar el menú principal y manejar las opciones."""
    clear_terminal()  # Limpia la terminal antes de mostrar cualquier mensaje
    print(ASCII_ART_PHISHING)
    print(f"{Colors.HEADER}[INFO]{Colors.ENDC} Herramienta de phishing - Menú\n")
    print(f"{Colors.WARNING}[1]{Colors.ENDC} Phishing por URL maliciosa")
    print(f"{Colors.WARNING}[2]{Colors.ENDC} Phishing por correo electrónico")
    print(f"{Colors.FAIL}[0]{Colors.ENDC} Salir\n")
    
    choice = input(f"{Colors.HEADER}[INFO]{Colors.ENDC} Elige una opción: ").strip()

    if choice == '1':
        phishing_by_url()
    elif choice == '2':
        phishing_by_email()
    elif choice == '0':
        print(f"{Colors.GREEN}[INFO]{Colors.ENDC} Saliendo de la herramienta...\n")
        exit()
    else:
        print(f"{Colors.FAIL}[ERROR]{Colors.ENDC} Opción no válida, intenta nuevamente.\n")

def main():
    """Función principal que ejecuta el menú y las opciones de phishing."""
    while True:
        display_menu()

if __name__ == "__main__":
    main()
