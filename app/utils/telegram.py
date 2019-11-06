import urllib.request
import urllib.parse
from settings import TELEGRAM_API_KEY, TELEGRAM_RECIPIENT_ID


class Telegram:
    def send_message(self, message):
        message = urllib.parse.quote(f'[csgo_autoupdater] {message}')
        url = f'https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TELEGRAM_RECIPIENT_ID}&text={message}'
        urllib.request.urlopen(url)