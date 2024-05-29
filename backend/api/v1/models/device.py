from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(15), nullable=False)

    def __init__(self, user_id, name, ip_address):
        self.user_id = user_id
        self.name = name
        self.ip_address = ip_address

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
            'user_id': self.user_id,
            'name': self.name,
            'ip_address': self.ip_address
               }
