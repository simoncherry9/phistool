<img src="https://github.com/user-attachments/assets/7792e1e3-39d0-428e-8eef-faca60fa5c0c" alt="Imagen de Phistool">

# phistool

Este repositorio contiene una herramienta de phishing que permite realizar ataques tanto por **correo electrónico** como por **URL maliciosa**. La herramienta también automatiza la configuración de **ngrok** para exponer servidores locales de forma sencilla.

## Características

- **Phishing por URL maliciosa**: Crea un servidor HTTP local con una plantilla de phishing y lo expone usando ngrok, generando una URL pública.
- **Phishing por correo electrónico**: Permite enviar correos electrónicos de phishing a direcciones específicas con un cuerpo personalizado o usando plantillas predefinidas.
- **Automatización de ngrok**: Configura y ejecuta ngrok automáticamente para exponer servidores locales sin necesidad de configuraciones manuales.

## Requisitos

- Python 3.x
- Cuenta en [ngrok](https://ngrok.com/) para exponer los servidores locales.
- Dependencias adicionales de Python, que se pueden instalar a través de `pip` o, si no están instaladas, el script `setup.py` se encargará de todo.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/phishing-toolkit.git
   cd phistool
   ```

2. **Instala las dependencias y configura ngrok automáticamente**:

    ```bash
    sudo python3 setup.py
    ```

    Sigue las instrucciones en pantalla para completar la configuración de ngrok.

## Uso

Para lanzar la herramienta, solo debes ejecutar:

```bash
python3 main.py
```

## Opciones

- **Phishing por URL maliciosa**: Crea un servidor con una plantilla de phishing y expone una URL utilizando ngrok.
- **Phishing por correo electrónico**: Envía un correo electrónico de phishing a la dirección que determines, con cuerpo personalizable o plantillas predefinidas.

## Plantillas

El repositorio incluye algunas plantillas de phishing, pero se irán agregando más en futuras actualizaciones. Si deseas contribuir o agregar más plantillas, puedes hacerlo creando un pull request.

## Contribuciones

Si deseas agregar más plantillas o mejorar la herramienta, puedes hacer un fork del repositorio, realizar tus cambios y abrir un pull request.

## Aviso Legal

Este software se proporciona con fines educativos y de investigación en ciberseguridad. No debes utilizarlo de manera maliciosa. Asegúrate de contar con el permiso adecuado antes de realizar pruebas de seguridad en cualquier sistema. El uso no autorizado puede ser ilegal y estar penado por la ley.

¡Gracias por usar esta herramienta! Si tienes alguna pregunta o encuentras algún error, no dudes en abrir un issue.
