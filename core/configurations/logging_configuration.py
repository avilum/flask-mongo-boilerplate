import os
from logging import *

from core.configurations.env import WORKING_DIRECTORY, DEBUG_MODE

LOGS_DIRECTORY_NAME = "logs"
LOGS_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGS_DIRECTORY_FULL_NAME = os.path.join(WORKING_DIRECTORY,
                                        LOGS_DIRECTORY_NAME)

# logging levels
DEFAULT_LOGGING_LEVEL = WARNING
ROTATING_FILE_HANDLER_LOGGING_LEVEL = DEBUG
STREAM_HANDLER_LEVEL = DEBUG if DEBUG_MODE else DEFAULT_LOGGING_LEVEL

BACKUP_LOGS_FILES_COUNT = 5
LOG_FILE_MAX_BYTES = 0.5 * 1000 * 1000  # 500KB
