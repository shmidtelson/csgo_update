import logging
from utils.main_loop import MainLoop
from utils.telegram import Telegram

if __name__ == '__main__':
    Telegram().send_message('CSGO автоапдейтер стартовал')
    logging.info('Started service')
    MainLoop()
