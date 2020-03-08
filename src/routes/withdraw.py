from flask_restful import Resource


class FeeHandler(Resource):
    def get(self):
        return {}