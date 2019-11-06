import os
from settings import PATH_TO_KEYS


class Key:
    def get(self, name):
        return os.path.join(PATH_TO_KEYS, name)
