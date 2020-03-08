import json


class AnchorInfo:
    __info_json: dict = None
    __config_json: dict = None

    def __init__(self, config_dir_path):
        if not AnchorInfo.info:
            self.load(config_dir_path)

    def load(self, config_dir_path):
        buffer = open(f"{config_dir_path}/info.json").read()
        self.__info_json = json.load(buffer)
        buffer = open(f"{config_dir_path}/info.json").read()
        self.__config_json = json.load(buffer)

    @property
    def info(self) -> dict:
        return self.__info_json

    @property
    def config(self) -> dict:
        return self.__config_json
