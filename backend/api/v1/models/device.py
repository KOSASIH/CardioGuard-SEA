from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name: str):
        self.name = name
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_health_data(self) -> List['HealthData']:
        return HealthData.query.filter_by(device_id=self.id).all()

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)

    def __init__(self, value: float, device_id: int):
        self.value = value
        self.device_id = device_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, value: float):
        self.value = value
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class MachineLearningModel:
    def fit(self, health_data: List['HealthData']):
        pass

    def predict(self, health_data: List['HealthData']):
        pass
