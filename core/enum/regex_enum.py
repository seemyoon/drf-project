from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-z]{,19}$',  # specify regex. it's a pattern
        'Only alpha characters are allowed'  # 2 arg - message. it's a msg
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
