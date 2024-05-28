from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from backend.api.v1.utils import validate_request_data
from backend.api.v1.models import User

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing email or password'}), 400

    user = User.query.filter_by(email=email).first()

    if not user or user.password != password:
        return jsonify({'message': 'Invalid email or password'}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({'access_token': access_token}), 200

@auth.route('/register', methods=['POST'])
@validate_request_data(User.schema)
def register():
    data = request.get_json()
    user = User(**data)
    user.save()

    return jsonify({'message': 'User registered successfully'}), 201
