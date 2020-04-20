from pproto_py import REGISTRY_COMMAND

PingCommand = "PING_COMMAND"
WhatIsTime = "WHAT_IS_TIME"
SendMeFail = "SEND_ME_FAIL"
EventMessage = "EVENT_MESSAGE"


# Каждая команда обязана иметь уникальное имя и UUID
PING_COMMAND  = REGISTRY_COMMAND(PingCommand,       "13903403-e03a-450f-a508-a8e1dc52e29e")
WHAT_IS_TIME  = REGISTRY_COMMAND(WhatIsTime,        "67adef57-ec0b-4efd-8161-bd21d4dc0a19")
SEND_ME_FAIL  = REGISTRY_COMMAND(SendMeFail,        "6c41ac94-cba0-472b-883f-b1ca8fbba309")
EVENT_MESSAGE = REGISTRY_COMMAND(EventMessage,      "9e5f61d9-bfaf-4282-b333-e09cff70fd01")
