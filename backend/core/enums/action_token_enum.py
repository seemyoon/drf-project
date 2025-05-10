from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    ACTIVATE = (
        'activate',  # name of token
        timedelta(minutes=30)
    )

    RECOVERY = (
        'activate',
        timedelta(minutes=10)
    )

    SOCKET = (
        'socket',
        timedelta(seconds=10) # it sufficiently to get response from BE and do request for connection token
    )

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
