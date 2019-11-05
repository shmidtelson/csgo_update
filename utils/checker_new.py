import json
import os
import urllib.request

from settings import PATH_TO_DATA


class CheckerNew:
    sha_from_api = ''
    sha_from_file = ''
    url = 'https://api.github.com/repos/SteamDatabase/GameTracking-CSGO/commits'

    def __init__(self):
        self.get_latest_from_api()
        self.get_latest_from_file()

    def get_latest_from_api(self):
        with urllib.request.urlopen(self.url) as f:
            data = f.read()
            encoding = f.info().get_content_charset('utf-8')

        result = json.loads(data.decode(encoding))

        self.sha_from_api = result[0].get('sha', None)

    def get_latest_from_file(self):
        with open(os.path.join(PATH_TO_DATA, 'latest_commit.txt')) as f:
            self.sha_from_file = f.read()

    def compare(self):
        return self.sha_from_api == self.sha_from_file

    def update_file(self):
        with open(os.path.join(PATH_TO_DATA, 'latest_commit.txt'), 'w+') as f:
            f.write(self.sha_from_api)
