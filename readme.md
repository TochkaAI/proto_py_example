# Тестовый пример использования библиотеки proto_py

## Пример использования:
- Клиент
```python
    from proto_py import TcpSocket

    # userCommands - имя модуля со списком команд
    # userCommandImpl - имя модуля с реализацией пользовательских команд
    import userCommandsImpl, userCommands
    
    ip_to_connect = <ip your server>
    port_to_connect = <port number>
    tcp_worker = TcpSocket(ip_to_connect, port_to_connect, userCommands, userCommandsImpl)
    tcp_worker.start()

    tcp_worker.get_current_connection().<COMMAND_NAME>_sync()
```
- Сервер
```python
    from proto_py import TcpServer
    
    # userCommands - имя модуля со списком команд
    # userCommandImpl - имя модуля с реализацией пользовательских команд
    import userCommandsImpl, userCommands

    listen_ip = <ip your server>
    listen_port = <port number>
    listening_worker = TcpServer(listen_ip, listen_port, userCommands, userCommandsImpl)
    listening_worker.run()

    for client_connection in listening_worker.connection_pool:
        client_connection.<COMMAND_NAME>_async()
```

## Примеры в коде:
Более подробную информацию можно найти в коде расположенном в репозитории
- Описание команд:
    - userCommands.py - список доступных для работы в протоколе команд
    - userCommandImpl.py - реализация этих самых команд
    
- Описание логики:
    - main_client.py - Клиентское приложение
    - main_server.py - Серверное приложение
    - logger.py - Конфигурация логов
