from pyproto import Message
from pyproto import BaseCommand
from .user_commands import HELLO


class Hello(BaseCommand):
    COMMAND_UUID = HELLO

    @staticmethod
    def initial(connection, content):
        msg = connection.create_command(Hello.COMMAND_UUID)
        print(content)
        msg.set_content({'message': content})
        return msg

    @staticmethod
    def answer(msg: Message):
        content = msg.get_content()
        return content
