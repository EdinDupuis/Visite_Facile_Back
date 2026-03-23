from flask import Flask
from controllers.visiteurs_controller import visiteurs_controller
from flask_cors import CORS
app = Flask(__name__)


CORS(app)

app.register_blueprint(visiteurs_controller)


if __name__ == '__main__':
    app.run()
