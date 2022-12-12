import logging
import datetime
import utils
from logging.handlers import TimedRotatingFileHandler

def build_default_logger():
    logger = logging.getLogger("Default Logger")
    logger.setLevel(logging.INFO)
    s_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '[%(levelname)s][%(filename)s: %(lineno)d][%(asctime)s]: [%(message)s]'
    )
    s_handler.setFormatter(formatter)

    logger.addHandler(s_handler)
    return logger


class SingleInstanceLogger:
    def __init__(self):
        self.logger = build_default_logger()

    def __getattr___(self, name):
        return getattr(self.logger, name)


_single_instance_logger = SingleInstanceLogger()

def build_logger(path):
    logger = logging.getLogger("New Logger")
    logger.setLevel(logging.INFO)
    utils.mkparents(path)

    s_handler = logging.StreamHandler()
    trf_handler = TimedRotatingFileHandler(
        filename=path,
        when="midnight",
        interval=1,
        backupCount=7,
        atTime=datetime.time(0,0,0,0)
    )

    formatter = logging.Formatter(
        "[%(levelname)s][%(filename)s: %(lineno)d][%(asctime)s: %(message)s]"
    )
    s_handler.setFormatter(formatter)
    trf_handler.setFormatter(formatter)
    logger.addHandler(s_handler)
    logger.addHandler(trf_handler)
    return logger
 

def setup_single_instance_logger(path):
     global _single_instance_logger
     _single_instance_logger.logger = build_logger(path)

if __name__ == "__main__":
    logger = SingleInstanceLogger()
    logger.info("")
    
