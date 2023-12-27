import logging


def get_logger():
    __logger = logging.getLogger("CoconutLogger")
    __logger.setLevel(logging.DEBUG)

    return __logger


def set_logger(__logger: logging.Logger):
    __formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(module)s:%(funcName)s %(message)s")
    __handler = logging.StreamHandler()
    __handler.setFormatter(__formatter)

    __logger.addHandler(__handler)
