"""Конфигурация логера"""
import sys
import logging


# Создание и конфигурация корневого логера
logger = logging.getLogger("demo-application")
logger.setLevel(logging.DEBUG)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    handlers=(
        logging.StreamHandler(sys.stdout),)
)
