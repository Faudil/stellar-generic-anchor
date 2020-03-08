from flask import Flask
from flask_restful import Resource, Api
from src.routes.fee import FeeHandler

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# api.add_resource(HelloWorld, "/info")
# api.add_resource(HelloWorld, "/withdraw")
api.add_resource(FeeHandler, "/fee")
api.add_resource(HelloWorld, "/transactions")




if __name__ == '__main__':
    app.run(debug=True)
