from datetime import datetime

from pproto_py import Message
from pproto_py import BaseCommand
from pproto_py.connection import Connection
from pproto_py.flags import ExecStatus, Type

from logger import logger
from userCommands import (
    PING_COMMAND,
    WHAT_IS_TIME,
    SEND_ME_FAIL,
    EVENT_MESSAGE
)


class PingCommand(BaseCommand):
    COMMAND_UUID = PING_COMMAND.uuid

    @staticmethod
    def initial(connection: Connection):
        msg = connection.create_command(PingCommand)
        msg.set_content({"data": "ping"})
        return msg

    @staticmethod
    def answer(msg: Message):
        if msg.get_content()['data'] == "pong":
            return True
        raise Exception('Incorrect client behavior')

    @staticmethod
    def handler(msg):
        ans = msg.get_answer_copy()
        data = msg.get_content()['data']
        if data != 'ping':
            ans.set_status(ExecStatus.Failed)
            ans.set_content(None)
        else:
            ans.set_content({"data": "pong"})
        ans.send_answer()


class WhatIsTime(BaseCommand):
    COMMAND_UUID = WHAT_IS_TIME.uuid

    @staticmethod
    def initial(connection):
        msg = connection.create_command(WhatIsTime)
        return msg

    @staticmethod
    def answer(msg: Message):
        return msg.get_content()['time_str']

    @staticmethod
    def handler(msg: Message):
        ans = msg.get_answer_copy()
        ans.set_content({"time_str": datetime.now().strftime("%H:%M:%S")})
        ans.send_answer()


class SendMeFail(BaseCommand):
    COMMAND_UUID = SEND_ME_FAIL.uuid

    @staticmethod
    def initial(connection):
        msg = connection.create_command(SendMeFail)
        return msg

    @staticmethod
    def handler(msg: Message):
        ans = msg.get_answer_copy()
        ans.set_status(ExecStatus.Failed)
        ans.send_answer()


class EventMessage(BaseCommand):
    COMMAND_UUID = EVENT_MESSAGE.uuid

    @staticmethod
    def initial(connection):
        msg = connection.create_event(EventMessage)
        return msg

    @staticmethod
    def handler(msg: Message):
        if msg.get_type() == Type.Event:
            logger.info("it's Event type Message")
        else:
            logger.info("It's not event")
