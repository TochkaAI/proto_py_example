import time
from threading import Thread
from pyproto import TcpSocket
from pyproto.config import RECONNECT_TIME_WAIT
from pyproto.connection import Connection

from .logger import logger
from . import user_commands, user_commands_impl


class TcpConnectionWorker:
    def __init__(self, ip, port):
        self.ip_to_connect = ip
        self.port_to_connect = port

        self.tcp_worker = TcpSocket(self.ip_to_connect, self.port_to_connect, user_commands, user_commands_impl)
        self.tcp_connection = None
        self.create_connection()

        if not self.tcp_connection:
            reconnecting_thread = Thread(target=create_start_connection, args=(self,))
            reconnecting_thread.daemon = True
            reconnecting_thread.start()

    @staticmethod
    def connection_restored(connection: Connection):
        logger.info(f'connection {connection.getpeername()} {connection.hist_fileno} was restored')

    @staticmethod
    def connection_is_dead(connection: Connection):
        logger.info(f'connection {connection.getpeername()} {connection.hist_fileno} was closed')
        connection.start_reconnecting(TcpConnectionWorker.connection_restored)

    def create_connection(self):
        self.tcp_worker.ip = self.ip_to_connect
        self.tcp_worker.port = self.port_to_connect
        connection = self.tcp_worker.connect(self.connection_is_dead)
        if connection and connection.is_connected():
            self.tcp_connection = connection
            return
        logger.info('not connected')

        return None

    def reconnect(self, ip, port):
        self.ip_to_connect = ip
        self.port_to_connect = int(port)
        if not self.tcp_connection or not self.tcp_connection.is_connected():
            self.create_connection()

        return self.tcp_connection

    def get_connection(self):
        return self.tcp_connection


def create_start_connection(connection_worker: TcpConnectionWorker):
    while not connection_worker.tcp_connection:
        connection_worker.create_connection()
        time.sleep(RECONNECT_TIME_WAIT)
