import os
import logging
from logging.handlers import RotatingFileHandler

from core.configurations.logging_configuration import LOGS_DIRECTORY_FULL_NAME, DEBUG, LOGS_FORMAT, Formatter, \
    BACKUP_LOGS_FILES_COUNT, LOG_FILE_MAX_BYTES, ROTATING_FILE_HANDLER_LOGGING_LEVEL, STREAM_HANDLER_LEVEL


class LoggerProvider(object):
    """
    Provides simple a simple loggers.
    The loggers are initialized according to the logging configuration.
    """

    loggers = {}

    @staticmethod
    def get_logger(logger_name):
        """
        Gets a logger by it's name.
        Creates the logger if it doesn't exist.
        :param logger_name: The name of the logger (identifier).
        :return: The logger instance.
        :returns: Logger
        """
        if not logger_name in LoggerProvider.loggers:
            LoggerProvider.loggers[logger_name] = LoggerProvider._get_logger(logger_name)
        return LoggerProvider.loggers[logger_name]

    @staticmethod
    def _get_logger(logger_name, logs_directory_path=LOGS_DIRECTORY_FULL_NAME):
        """
        Creates a logger with rolling file handler,
        Or returns the logger if it already exists.

        :param logger_name: The name of the logger
        :param logs_directory_path: The path of the directory that the logs will be written to.

        :return: An initialized logger instance.
        returns: Logger
        """

        # Creating the logs folder if its doesn't exist
        if not os.path.exists(logs_directory_path):
            os.mkdir(logs_directory_path)

        logger = logging.getLogger(logger_name)
        logger.setLevel(DEBUG)
        formatter = Formatter(LOGS_FORMAT)

        # The file handler will log everything (debug)
        rotating_file_handler = RotatingFileHandler(
            os.path.join(logs_directory_path, '{0}.log'.format(logger_name)), maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=BACKUP_LOGS_FILES_COUNT)

        # The stream handler will log only warnings.
        stream_handler = logging.StreamHandler()

        # Setting levels
        rotating_file_handler.setLevel(ROTATING_FILE_HANDLER_LOGGING_LEVEL)
        stream_handler.setLevel(STREAM_HANDLER_LEVEL)

        # Setting formatters
        rotating_file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        # Add the log message handler to the logger
        logger.addHandler(rotating_file_handler)
        logger.addHandler(stream_handler)
        return logger
