from pyproto import BaseCommand
from .user_commands import HELLO


class Hello(BaseCommand):
    COMMAND_UUID = HELLO

    @staticmethod
    def handler(msg):
        ans = msg.get_answer_copy()
        ans.set_content('World!')
        ans.send_answer()
