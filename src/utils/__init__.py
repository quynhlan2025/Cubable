import logging
import platform

from colorlog import ColoredFormatter

os_name = platform.system()  # Mac: Darwin | Win: Windows
LOG_LEVEL = logging.INFO
LOG_FORMAT = "\t%(asctime)-6s.%(msecs)03d %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
LOG_FORMAT_WIN = "\t%(asctime)-6s %(levelname)7s | %(message)s"
logging.root.setLevel(LOG_LEVEL)
logger = logging.getLogger('pythonConfig')


def create_new_handler_logger(log_level):
    logger.propagate = False
    if not logger.handlers:
        stream = logging.StreamHandler()  # pylint: disable=invalid-name
        stream.setLevel(log_level)
        if os_name == "Windows":
            formatter = logging.Formatter(LOG_FORMAT_WIN, "%H:%M:%S")
            stream.setFormatter(formatter)
        else:
            stream.setFormatter(ColoredFormatter(LOG_FORMAT, "%H:%M:%S"))  # "%Y-%m-%d %H:%M:%S"
        logger.setLevel(log_level)
        logger.addHandler(stream)


create_new_handler_logger(LOG_LEVEL)
