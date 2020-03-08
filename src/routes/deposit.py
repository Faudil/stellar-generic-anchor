from flask_restful import Resource
from flask_restful import Resource, reqparse
from src.data.AnchorInfo import AnchorInfo

parser = reqparse.RequestParser()
parser.add_argument("asset_code")
parser.add_argument("account")
parser.add_argument("memo_type", store_missing=False)
parser.add_argument("memo", store_missing=False)
parser.add_argument("email_address", store_missing=False)
parser.add_argument("type", store_missing=False)
parser.add_argument("wallet_name", store_missing=False)
parser.add_argument("wallet_url", store_missing=False)
parser.add_argument("lang", store_missing=False)


class DepositHandler(Resource):
    def get(self):
        af = AnchorInfo(None)
        info = af.info
        config = af.config
        args = parser.parse_args()
        if args.asset_code not in info[args.operation]:
            return 400, {"error": f"asset_code {args.operation} not recognized"}
        action_info: dict = info[args.operation][args.asset_code]
        if action_info["enabled"]:
            return 400, {"error": f"Anchor has disabled asset {args.asset_code}"}
        return 200, {**config["deposit"][args.asset_code], **info["deposit"][args.asset_code]}
