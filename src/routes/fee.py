from flask import request
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("operation")
parser.add_argument("type", store_missing=False)
parser.add_argument("asset_code")
parser.add_argument("amount", type=float)


class FeeHandler(Resource):
    def get(self):
        args = parser.parse_args()
        return 200, {"status": "ok"}
