import shelve
from choosing import game_settings


class Save:
    def __init__(self):
        self.file = shelve.open('data')
        self.info = game_settings()

    def save(self):
        self.file['info'] = self.info
        self.file['number'] = 25

    def get(self):
        num = self.file['number']
        print(num)
        print(self.file['info'])

    def __del__(self):
        self.file.close()
