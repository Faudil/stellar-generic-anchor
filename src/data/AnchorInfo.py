import json


class AnchorInfo:
    __json = None

    def __init__(self, file_path):
        if not AnchorInfo.json:
            self.load(file_path)

    def load(self, file_path):
        buffer = open(file_path).read()
        self.__json = json.load(buffer)

    @property
    def json(self):
        return self.__json
