from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.interact_with_nano_service import InteractWithNanoService

interact_with_nano_blueprint = Blueprint('interact_with_nano_blueprint', __name__)


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401


@interact_with_nano_blueprint.route('/getFaceImageFromNano', methods=['GET'])
@jwt_required()
def get_face_image_from_nano(signal=1):
    result = InteractWithNanoService.get_face_image_from_nano_service(signal)
    if result is None:
        return jsonify(message='后台交互失败'), 500
    else:
        return jsonify(result), 200
