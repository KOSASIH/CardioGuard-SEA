from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    heart_rate = db.Column(db.Float, nullable=False)
    blood_pressure = db.Column(db.Float, nullable=False)
    glucose_level = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, device_id, heart_rate, blood_pressure, glucose_level):
        self.device_id = device_id
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.glucose_level = glucose_level

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'device_id': self.device_id,
            'heart_rate': self.heart_rate,
            'blood_pressure': self.blood_pressure,
            'glucose_level': self.glucose_level,
            'created_at': self.created_at
        }
