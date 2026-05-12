from http.server import HTTPServer

from config import HOSTNAME, SERVERPORT
from models.server import MyServer

if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((HOSTNAME, SERVERPORT), MyServer)
    print()
    print("Server started http://%s:%s" % (HOSTNAME, SERVERPORT))
    print()

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")