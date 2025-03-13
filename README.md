# Alerta-de-inicio-de-sesion

📌 Descripción
Este script en Python envía una alerta a Telegram cuando se inicia sesión en el equipo. Además, captura una foto con la cámara de la computadora y la envía junto con la alerta.

📌 Requisitos
Antes de ejecutar el script, asegúrate de tener instaladas las siguientes dependencias:

🔹 Instalación de librerías necesarias
Ejecuta el siguiente comando en PowerShell o CMD:

pip install opencv-python requests

🔹 Verifica que la cámara esté habilitada
Abre la aplicación "Cámara" de Windows para comprobar que funciona.
Si la cámara está apagada, actívala en Configuración de Windows:
Win + I → Privacidad y Seguridad → Cámara → Permitir acceso a aplicaciones de escritorio.

📌 Configuración
🔹 Variables a configurar en el script
Antes de ejecutar el script, reemplaza los siguientes valores:

TOKEN = "TU_BOT_TOKEN_AQUI"  # Token del bot de Telegram
CHAT_ID = "TU_CHAT_ID_AQUI"  # ID del chat donde se enviará la alerta

📌 Cómo Ejecutarlo Automáticamente al Iniciar Sesión
Puedes configurar el script para que se ejecute automáticamente cuando inicies sesión en Windows.

🔹 Usar el Programador de Tareas

Abre el Programador de Tareas (taskschd.msc).

Crea una nueva tarea:

Nombre: Alerta de Inicio de Sesión

Ejecutar con los privilegios más altos: ✅

Disparador (Cuándo se ejecutará):

Evento: "Al iniciar sesión".

Acción (Qué hará):

Iniciar un programa.

Programa: python.exe

Argumentos: "C:\Scripts\alerta_inicio_sesion.py"

Iniciar en: C:\Scripts\

Guarda la tarea y prueba reiniciando tu equipo.
