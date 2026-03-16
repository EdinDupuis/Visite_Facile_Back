from flask import Flask
from controllers import visiteurs_controller as vc

app = Flask(__name__)

app.register_blueprint(vc.visiteurs_controller)

if __name__ == '__main__':
    app.run()
