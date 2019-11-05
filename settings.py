import os
import logging
import logging.handlers
import time

SERVER_LIST = [
    {
        'server_name': 'retake1',
        'ip': '212.109.193.210',
        'port': '22556',
        'user': 'root',
        'command': 'cd /opt/retake1 && docker-compose -f updater.yml up'
    },
    {
        'server_name': 'retake2',
        'ip': '94.250.255.217',
        'port': '22556',
        'user': 'root',
        'command': 'cd /opt/retake2 && docker-compose -f updater.yml up'
    },
    {
        'server_name': 'retake3',
        'ip': '185.209.29.144',
        'port': '22556',
        'user': 'root',
        'command': 'cd /opt/retake3 && docker-compose -f updater.yml up'
    },
]

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PATH_TO_KEYS = os.path.join(ROOT_PATH, 'keys')
PATH_TO_DATA = os.path.join(ROOT_PATH, 'data')
PATH_TO_LOGS = os.path.join(ROOT_PATH, 'logs')


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
