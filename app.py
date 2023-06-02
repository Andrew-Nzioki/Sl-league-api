from flask import Flask
from flask_restful import Api

from flask_jwt import JWT

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'andrew'
api = Api(app)

# initiliaze the method or rather create a new endpoibt /auth
jwt = JWT(app, authenticate, identity)  # /auth
# a class that inherits a resource ClassName(Resource):
# api.add_resource
# flask Restful doesn't need jsonify


if __name__ =="__main__":
    app.run(port=5000,debug=True)