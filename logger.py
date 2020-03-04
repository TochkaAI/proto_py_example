"""Конфигурация логера"""
import sys
import logging


# Создание и конфигурация корневого логера
logger = logging.getLogger("example")
logger.setLevel(logging.DEBUG)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    handlers=(
        # logging.FileHandler("/var/opt/digital-earth/log/rest-api.log", mode='a'),
        logging.StreamHandler(sys.stdout))
)

# Установка значения уровня логирования для pyproto
logging.getLogger("pyproto").setLevel(logging.DEBUG)

# Установка значения уровня логирования для client_logger
logging.getLogger("client_logger").setLevel(logging.DEBUG)

# Установка значения уровня логирования для server_logger
logging.getLogger("server_logger").setLevel(logging.DEBUG)
