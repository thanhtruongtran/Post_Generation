import os
import json
import logging
from logging.handlers import RotatingFileHandler

FORMATTER = logging.Formatter(fmt='[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
                              datefmt='%m-%d-%Y %H:%M:%S %Z')
LOG_FILE = 'logging.log'


def get_console_handler():
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=2000, backupCount=1)
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    # logger.addHandler(get_file_handler())
    return logger


def write_file(folder_direction, name, file):
    if not os.path.exists(f'data/log_file/{folder_direction}'):
        try:
            os.makedirs(f'data/log_file/{folder_direction}')
        except Exception as ex:
            with open(f'data/log_file/{folder_direction}/{name}.json', 'a') as f:
                f.write(json.dumps(file))
                f.write("\n")
            
    with open(f'data/log_file/{folder_direction}/{name}.json', 'a') as f:
                f.write(json.dumps(file))
                f.write("\n")
    