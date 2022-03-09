from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from views import UsersCollection
from views import UserItem

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Users-Administration-Python-Flask-REST-API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

CORS(app)
api = Api(app)

api.add_resource(UsersCollection, '/users')
api.add_resource(UserItem, '/users/<int:user_id>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)