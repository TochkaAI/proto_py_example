"""Файл реализации функционала сервера protopy"""
from threading import Thread
import time

# Импорт описания и реализации пользовательских команд
import userCommandsImpl, userCommands
# Импорт основной сущности работы с protopy для сервера
from proto_py import TcpServer

# Работа с логирование. В данном случае логгер настроен на отображение информации в консоли
import logger


if __name__ == '__main__':
    # Этот сервер будет слушать на таком ip и на таком порту
    listen_ip = '127.0.0.1'
    listen_port = 38015

    # Создаём объект сущности TcpServer для дальнейшего прослушивания и созданию входящих подключений
    listening_worker = TcpServer(listen_ip, listen_port, userCommands, userCommandsImpl)
    # Запускаем прослушивание порта
    listening_worker.run()

    # Дальше следует импровизированная логика работы
    # Этот цикл будет запущен в отдельном потоке,
    # и будет с периодичностью раз в 5 секунд отправлять команду PING_COMMAND
    def ping_loop():
        # Бесконечный цикл
        while True:
            # Ожидание 5 секунд
            time.sleep(5)
            # Перебираем все подключения которые у нас есть
            for connection in listening_worker.connection_pool.values():
                # в каждое подключение отправляем команду
                connection.PING_COMMAND_async()
            time.sleep(0.2)
            print('==='*10)


    # Запуск в отдельном потоке
    thread = Thread(target=ping_loop)
    thread.setDaemon(True)
    thread.start()

    # Просто ожидаем от пользователя пока он закроет приложение
    try:
        while True:
            value = input("INPUT: ")
            if value == 'exit':
                break
    finally:
        listening_worker.stop()
