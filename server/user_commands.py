"""
Список констант с существующими базовыми командами
"""
import sys


Hello = "HELLO"


def REGISTRY_COMMAND_SINGLPROC(name, uuid):
    setattr(sys.modules[__name__], name, uuid)


REGISTRY_COMMAND_SINGLPROC(Hello,                    "286b6b46-30d8-4b44-8b64-285510522423")
