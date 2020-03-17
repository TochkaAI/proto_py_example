"""Файл реализации функционала клиента pyproto"""

# Импорт описания и реализации пользовательских команд
import userCommandsImpl, userCommands
# Импорт основной сущности работы с pyproto для клиента
from pyproto import TcpSocket

# Работа с логирование. В данном случае логгер настроен на отображение информации в консоли
import logger


if __name__ == '__main__':
    # Этот клиент будет подключаться к серверу с данными параметрами
    ip_to_connect = '127.0.0.1'
    port_to_connect = 38015

    # Создаём объект сущности TcpSocket для дальнейшего подключения к серверу и обмена командами
    tcp_worker = TcpSocket(ip_to_connect, port_to_connect, userCommands, userCommandsImpl)
    # Запускаем работу, клиент будет пытаться подключится к серверу автоматически, в случае его недоступности
    # Так же, он автоматически будет пытаться восстановить подключение после разрыва
    tcp_worker.start()
    # Если после установки соединения необходимо выполнение каких-то действий, в метод start можно передать обработчики
    # connect_handler, restore_handler, disconnect_handler
    # Установленно первичное подключение, восстановлено подключение, произошёл разрыв связи - соответственно

    # Дальше следует импровизированная логика работы с клиентом через ввод команд в консоли
    try:
        while True:
            value = input("INPUT: ")
            if value == 'exit':
                break
            if value == 't':
                # Команда WHAT_IS_TIME выполняет синхронно,
                # результатом выполнения команды, является строка с текущим временем,
                # которая была получена с удалённого сервера
                time_str = tcp_worker.get_current_connection().WHAT_IS_TIME_sync()
                print(time_str)
            else:
                print('Unkwon command, pls reenter')
    finally:
        tcp_worker.disconnect()
