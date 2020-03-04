from pyproto import TcpServer
from server import user_commands, user_commands_impl
from client.worker import TcpConnectionWorker


if __name__ == '__main__':
    SERVER = TcpServer('127.0.0.1', 38000, user_commands, user_commands_impl).run()
    CLIENT = TcpConnectionWorker('127.0.0.1', 38000)

    conn = CLIENT.get_connection()
    answer = conn.HELLO_sync("Hello")
    print(answer)
