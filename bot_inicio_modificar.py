import cv2
import os
import requests
import platform
import getpass
from datetime import datetime

# Configuración del bot de Telegram
TOKEN = "TU_BOT_TOKEN_AQUI"
CHAT_ID = "TU_CHAT_ID_AQUI"

# 🔹 Obtener usuario y nombre del equipo
usuario = getpass.getuser()
equipo = platform.node()
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 🔹 Ruta donde se guardará la foto
foto_path = os.path.join(os.environ["USERPROFILE"], "Pictures", "foto_alerta.jpg")

# 🔹 Capturar la foto con la cámara
def tomar_foto():
    try:
        cam = cv2.VideoCapture(0)  # Abrir la cámara (0 = cámara predeterminada)
        ret, frame = cam.read()  # Capturar el frame
        if ret:
            cv2.imwrite(foto_path, frame)  # Guardar la imagen
            print("✅ Foto tomada correctamente.")
        else:
            print("❌ No se pudo capturar la foto.")
        cam.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"❌ Error al tomar la foto: {e}")

# 🔹 Enviar la foto a Telegram
def enviar_foto():
    if os.path.exists(foto_path):
        url_foto = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        files = {"photo": open(foto_path, "rb")}
        data = {"chat_id": CHAT_ID}
        try:
            response = requests.post(url_foto, files=files, data=data)
            if response.status_code == 200:
                print("✅ Foto enviada correctamente a Telegram.")
            else:
                print(f"❌ Error al enviar la foto: {response.text}")
        except Exception as e:
            print(f"❌ Error al enviar la foto: {e}")
    else:
        print("❌ No se encontró la foto para enviar.")

# 🔹 Crear mensaje de alerta
mensaje = f"""
⚠️ *ALERTA INICIO DE SESIÓN* ⚠️

👤 Usuario: *{usuario}*
💻 Equipo: *{equipo}*
📅 Fecha y hora: *{fecha}*
"""

# 🔹 Enviar el mensaje a Telegram
url_mensaje = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": mensaje,
    "parse_mode": "Markdown",
    "disable_web_page_preview": True
}

try:
    requests.post(url_mensaje, json=payload)
    print("✅ Alerta enviada a Telegram.")
except requests.RequestException as e:
    print(f"❌ Error al enviar la alerta: {e}")

# 🔹 Tomar la foto y enviarla
tomar_foto()
enviar_foto()