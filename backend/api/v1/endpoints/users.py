from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.api.v1.utils import validate_request_data
from backend.api.v1.models import User

@users.route('/', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify(user.to_dict()), 200

@users.route('/', methods=['PUT'])
@jwt_required()
@validate_request_data(User.schema)
def update_current_user():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    user.update(**data)

    return jsonify({'message': 'User updated successfully'}), 200

@users.route('/', methods=['DELETE'])
@jwt_required()
def delete_current_user():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    user.delete()

    return jsonify({'message': 'User deleted successfully'}), 200
