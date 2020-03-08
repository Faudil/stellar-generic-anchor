from flask_restful import Resource, reqparse

from src.data.AnchorInfo import AnchorInfo

parser = reqparse.RequestParser()
parser.add_argument("operation")
parser.add_argument("type", store_missing=False)
parser.add_argument("asset_code")
parser.add_argument("amount", type=float)


class FeeHandler(Resource):
    def get(self):
        info = AnchorInfo(None).info
        args = parser.parse_args()
        if args.operation not in info.keys():
            return 400, {"error": f"operation not recognized {args.operation}"}
        if args.asset_code not in info[args.operation]:
            return 400, {"error": f"asset_code {args.operation} not recognized"}
        action_info: dict = info[args.operation][args.asset_code]
        if action_info["enabled"]:
            return 400, {"error": f"Anchor has disabled asset {args.asset_code} for {args.operation}"}
        min_amount = action_info["min_amount"] if "min_amount" in action_info.keys() else 0
        if args.amount < min_amount:
            return 400, {"error": f"Amount {args.amount} is inferior than minimum"
                                  f" {info[args.operation]} amount {min_amount}"}
        amount = args.amount
        fee_fixed = action_info["fee_fixed"] if "fee_fixed" in action_info.keys() else 0
        fee_percent = action_info["fee_percent"] if "fee_percent" in action_info.keys() else 0
        return 200, {"fee": fee_fixed + (amount * (fee_percent / 100))}
