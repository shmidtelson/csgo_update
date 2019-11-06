import os
import logging
import logging.handlers
import time
import json

from dotenv import load_dotenv
load_dotenv()

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_KEYS = os.path.join(ROOT_PATH, 'keys')
PATH_TO_DATA = os.path.join(ROOT_PATH, 'data')
PATH_TO_LOGS = os.path.join(ROOT_PATH, 'logs')

SERVER_LIST = json.loads(open(os.path.join(PATH_TO_DATA, 'servers.json')).read())

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_RECIPIENT_ID = os.getenv("TELEGRAM_RECIPIENT_ID")

def log_setup():
    log_handler = logging.handlers.TimedRotatingFileHandler(os.path.join(PATH_TO_LOGS, 'app.log'), when='D', interval=1)
    formatter = logging.Formatter(
        '%(asctime)s [%(process)d]: %(message)s',
        '%b %d %H:%M:%S')
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
