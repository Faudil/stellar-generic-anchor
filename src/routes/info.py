from flask_restful import Resource

from src.data.AnchorInfo import AnchorInfo


class InfoHandler(Resource):
    def get(self):
        info = AnchorInfo(None).info
        return 200, info
