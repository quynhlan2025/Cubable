import time

from src.utils import logger


def sleep(seconds: int, log: str = None):
    if log:
        logger.info(" - %s" % log)
    time.sleep(seconds)
