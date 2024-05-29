from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from config import Config
from utils.database import db
from utils.auth import auth
from utils.machine_learning import predict_risk

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)
ma = Marshmallow(app)

# Import routes
from api.v1.endpoints.auth import auth_blueprint
from api.v1.endpoints.users import user_blueprint
from api.v1.endpoints.devices import device_blueprint
from api.v1.endpoints.health_data import health_data_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(device_blueprint)
app.register_blueprint(health_data_blueprint)

@app.route('/')
def index():
    return 'Welcome to CardioGuard-SEA API'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = data.get('age')
    gender = data.get('gender')
    bp = data.get('bp')
    chol = data.get('chol')
    fbs = data.get('fbs')
    bmi = data.get('bmi')
    htn = data.get('htn')
    dm = data.get('dm')
    smoker = data.get('smoker')
    region = data.get('region')

    risk = predict_risk(age, gender, bp, chol, fbs, bmi, htn, dm, smoker, region)

    return jsonify({'risk': risk})

if __name__ == '__main__':
    app.run(debug=True)
