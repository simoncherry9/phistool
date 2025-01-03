# Phistool

![Imagen de Phistool](https://github.com/user-attachments/assets/7792e1e3-39d0-428e-8eef-faca60fa5c0c)

Phistool es una herramienta de **phishing** que te permite realizar ataques de **phishing por correo electrónico** y **por URL maliciosa**. La herramienta también automatiza la configuración de **ngrok** para exponer servidores locales de forma rápida y sencilla.

---

## 📋 Características

- **Phishing por URL maliciosa**: Crea un servidor HTTP con una plantilla de phishing y lo expone usando ngrok, generando una URL pública.
- **Phishing por correo electrónico**: Envía correos electrónicos de phishing a direcciones específicas, con un cuerpo personalizable o usando plantillas predefinidas.
- **Automatización de ngrok**: Configura y ejecuta ngrok automáticamente para exponer servidores locales sin necesidad de configuraciones manuales.

---

## ⚙️ Requisitos

- Python 3.x
- Cuenta en [ngrok](https://ngrok.com/) para exponer servidores locales.
- Dependencias de Python, que se instalan automáticamente mediante `setup.py`.
- Cuenta de Gmail configurada con una contraseña de aplicaciones para poder enviar correos electrónicos.

---

## 🛠️ Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/simoncherry9/phistool.git
   cd phistool
   ```

2. **Instala las dependencias y configura ngrok automáticamente**:

   ```bash
   sudo python3 setup.py
   ```

   Sigue las instrucciones en pantalla para completar la configuración de ngrok.

---

## 🚀 Uso

Para iniciar la herramienta, solo ejecuta:

```bash
python3 main.py
```

---

## 🌐 Opciones

- **Phishing por URL maliciosa**: Crea un servidor con una plantilla de phishing y expone una URL utilizando ngrok.
- **Phishing por correo electrónico**: Envía un correo electrónico de phishing a la dirección que determines, con cuerpo personalizable o plantillas predefinidas.

---

## 📂 Plantillas

El repositorio incluye algunas plantillas de phishing, pero se irán agregando más en futuras actualizaciones. Si deseas contribuir o agregar más plantillas, puedes hacerlo creando un pull request.

---

## 🤝 Contribuciones

Si deseas mejorar el proyecto o agregar nuevas plantillas, puedes hacer un fork del repositorio, realizar tus cambios y abrir un pull request. ¡Las contribuciones son bienvenidas!

---

## 👤 Autor

Este proyecto fue desarrollado por **Saimonch16**.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo LICENSE para más detalles.

---

## ⚠️ Aviso Legal

Este software se proporciona con fines educativos y de investigación en ciberseguridad. No debe usarse para fines maliciosos. Asegúrate de contar con el permiso adecuado antes de realizar pruebas de seguridad en cualquier sistema. El uso no autorizado puede ser ilegal y estar penado por la ley.

---

¡Gracias por usar Phistool! Si tienes alguna pregunta o encuentras algún error, no dudes en abrir un issue.
