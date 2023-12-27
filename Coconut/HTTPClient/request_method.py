from enum import Enum


class RequestMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    HEAD = 3
    DELETE = 4
    PATCH = 5
    OPTIONS = 6
