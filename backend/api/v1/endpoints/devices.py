from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.api.v1.utils import validate_request_data
from backend.api.v1.models import Device

@devices.route('/', methods=['POST'])
@jwt_required()
@validate_request_data(Device.schema)
def create_device():
    data = request.get_json()
    user_id = get_jwt_identity()
    device = Device(user_id=user_id, **data)
    device.save()

    return jsonify(device.to_dict()), 201

@devices.route('/<int:device_id>', methods=['GET'])
@jwt_required()
def get_device(device_id):
    user_id = get_jwt_identity()
    device = Device.query.get_or_404(device_id)

    if device.user_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify(device.to_dict()), 200

@devices.route('/<int:device_id>', methods=['PUT'])
@jwt_required()
@validate_request_data(Device.schema)
def update_
