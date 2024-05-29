from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.device import Device
from models.health_data import HealthData

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/cardioguard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

        # Add test data
        user1 = User(email='user1@example.com', password='password1', name='User 1')
        user1.save()

        user2 = User(email='user2@example.com', password='password2', name='User 2')
        user2.save()

        device1 = Device(user_id=user1.id, name='Device 1', ip_address='192.168.1.1')
        device1.save()

        device2 = Device(user_id=user2.id, name='Device 2', ip_address='192.168.1.2')
        device2.save()

        health_data1 = HealthData(device_id=device1.id, heart_rate=80, blood_pressure=120, glucose_level=100)
        health_data1.save()

        health_data2 = HealthData(device_id=device2.id, heart_rate=90, blood_pressure=130, glucose_level=110)
        health_data2.save()
