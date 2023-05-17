import logging
from logging.handlers import RotatingFileHandler
from emp.utils.config import Config
from emp.utils.singleton import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        config: Config = Config()
        self.logger = logging.getLogger('EMP')

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_formatter = logging.Formatter(
            fmt='[%(asctime)s] %(name)s [%(levelname)s]: %(message)s', datefmt='%y-%m-%d %H:%M:%S')

        # Create a file handler
        rotating_file_handler = RotatingFileHandler(
            filename=config.get_log_file(), mode='wa', maxBytes=1024000, backupCount=30)
        stream_handler = logging.StreamHandler()

        # Set log level
        log_level = self.get_level(config.get_log_level())
        self.logger.setLevel(log_level)

        stream_handler.setLevel(log_level)
        rotating_file_handler.setLevel(log_level)

        # Create a formatter and add it to the handler
        stream_handler.setFormatter(formatter)
        rotating_file_handler.setFormatter(file_formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(rotating_file_handler)

    @staticmethod
    def get_level(level):
        try:
            dict = {
                'CRITICAL': logging.CRITICAL,
                'DEBUG': logging.DEBUG,
                'ERROR': logging.ERROR,
                'FATAL': logging.FATAL,
                'INFO': logging.INFO,
                'WARNING': logging.WARNING,
            }

            return dict[level]
        except KeyError:
            raise Exception("Invalid log level")

    def info(self, str):
        self.logger.info(str)

    def debug(self, str):
        self.logger.debug(str)

    def error(self, str):
        self.logger.error(str)

    def critical(self, str):
        self.logger.critical(str)

    def warning(self, str):
        self.logger.warning(str)

    def fatal(self, str):
        self.logger.fatal(str)
