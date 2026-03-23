from flask import Flask
from controllers import visiteurs_controller as vc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(vc.visiteurs_controller)



if __name__ == '__main__':
    app.run()
