from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HTML_DIR = BASE_DIR / "templates"
CSS_DIR = BASE_DIR / "css"
JS_DIR = BASE_DIR / "js"
IMG_DIR = BASE_DIR / "img"

HOSTNAME = "localhost" # Адрес для доступа по сети
SERVERPORT = 8080 # Порт для доступа по сети

