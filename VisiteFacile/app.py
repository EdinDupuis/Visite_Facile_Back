from flask import Flask

from controllers import visiteurs_controller as vc
from flask_cors import CORS
from dotenv import dotenv_values

env_values = dotenv_values(".env")
CORS_ORIGIN = env_values["CORS_ORIGIN"]
app = Flask(__name__)
CORS(app, origins=CORS_ORIGIN)
app.register_blueprint(vc.visiteurs_controller)

if __name__ == '__main__':
    app.run()