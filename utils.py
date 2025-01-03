import os

# Colores para la terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# ASCII art para la herramienta de phishing
ASCII_ART_PHISHING = f"""
{Colors.BLUE}
        _     _     _              _ 
  _ __ | |__ (_)___| |_ ___   ___ | |
 | '_ \| '_ \| / __| __/ _ \ / _ \| |
 | |_) | | | | \__ \ || (_) | (_) | |
 | .__/|_| |_|_|___/\__\___/ \___/|_|   
 |_|                                 
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
