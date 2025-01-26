from flask import Flask
from flask_smorest import Api # type: ignore
from resources.Item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

# for registering these created Blueprint with the api
# Write a configuration options for the API

# this is for if their any exception is occur in the extension of class
# then propagate it in the main app
app.config["PROPAGATE_EXCEPTION"] = True

# flask_smorest configurations
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
# here OPENAPI_VERSION it is a standard default
app.config["OPENAPI_VERSION"] = "3.0.3"

# this is for url prefix -> url start with
app.config["OPENAPI_URL_PREFIX"] = "/"

# This is for UI of the website
app.config["OPENAPI_SWAGGER_UI_PATH"] ="/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# this is for the connect the flask smorest extension with Flask app
api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
