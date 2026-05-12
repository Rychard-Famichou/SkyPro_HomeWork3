import os
from http.server import BaseHTTPRequestHandler

from config import HTML_DIR, CSS_DIR, JS_DIR, IMG_DIR


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def get_file_content(self, file_path):
        """Вспомогательный метод для чтения файлов"""
        with open(file_path, "rb") as file:
            return file.read()

    def do_GET(self):
        """Метод для обработки GET-запросов"""
        # 1. Обработка CSS
        if self.path.startswith("/css/"):
            file_name = os.path.basename(self.path)
            file_path = CSS_DIR / file_name
            if file_path.exists():
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()
                self.wfile.write(self.get_file_content(file_path))
            else:
                self.send_error(404, "CSS Not Found")
            return

        # 2. Обработка JS
        if self.path.startswith("/js/"):
            file_name = os.path.basename(self.path)
            file_path = JS_DIR / file_name
            if file_path.exists():
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(self.get_file_content(file_path))
            else:
                self.send_error(404, "JS Not Found")
            return

        # 2.5. Обработка изображений
        if self.path.startswith("/img/"):
            file_name = os.path.basename(self.path)
            file_path = IMG_DIR / file_name

            if file_path.exists():
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                self.wfile.write(self.get_file_content(file_path))
            else:
                self.send_error(404, "Image Not Found")
            return

        # 3. Обработка HTML
        path = self.path.strip("/")

        if path == "":
            file_name = "index.html"
        else:
            file_name = f"{path}.html"

        file_path = HTML_DIR / file_name

        if file_path.exists():
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.get_file_content(file_path))
        else:
            self.send_error(404, "Page Not Found")

    def do_POST(self):
        """Метод для обработки POST-запросов"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print()
        print(f"Получены данные: {post_data.decode('utf-8')}")
        print()
        self.send_response(200)
        self.end_headers()
