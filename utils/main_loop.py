import time
import logging

from settings import log_setup
from utils.checker_new import CheckerNew
from utils.send_command import SendCommands


log_setup()

class MainLoop:
    def __init__(self):
        while True:
            try:
                cn = CheckerNew()
                if not cn.compare():
                    cn.update_file()
                    SendCommands()
                raise Exception('TEst')
            except Exception as e:
                logging.info(f'Error {e}')
            time.sleep(60)