"""
Список констант с существующими базовыми командами
"""


Hello = "HELLO"


class REGISTRY_COMMAND_SINGLPROC:
    commands_names = []
    commands_uuids = []

    def __init__(self, name, uuid):
        self.name = name
        self.uuid = uuid
        if name in REGISTRY_COMMAND_SINGLPROC.commands_names:
            raise ValueError(f'Command name {name} is not unique')
        if uuid in REGISTRY_COMMAND_SINGLPROC.commands_uuids:
            raise ValueError(f'Command uuid {uuid} is not unique')
        REGISTRY_COMMAND_SINGLPROC.commands_names.append(name)
        REGISTRY_COMMAND_SINGLPROC.commands_uuids.append(uuid)

    # @staticmethod
    # def get_by_id(id_):
    #     return A.commands.get(id_)


# def REGISTRY_COMMAND_SINGLPROC(name, uuid):
#     setattr(sys.modules[__name__], name, uuid)


HELLO = REGISTRY_COMMAND_SINGLPROC(Hello,                    "286b6b46-30d8-4b44-8b64-285510522423")
# HELLO1 = REGISTRY_COMMAND_SINGLPROC(Hello,                    "286b6b46-30d8-4b44-8b64-285510522423")
# REGISTRY_COMMAND_SINGLPROC(Hello,                    "286b6b46-30d8-4b44-8b64-285510522423")
# REGISTRY_COMMAND_SINGLPROC(Hello,                    "286b6b46-30d8-4b44-8b64-285510522423")
# REGISTRY_COMMAND_SINGLPROC(Hello,                    "286b6b46-30d8-4b44-8b64-285510522423")
