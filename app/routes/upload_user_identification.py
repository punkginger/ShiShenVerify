from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.upload_user_identification_service import UploadUserIdentificationService

upload_user_identification_blueprint = Blueprint('upload_user_identification_blueprint', __name__)


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401


@upload_user_identification_blueprint.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    user_info = request.json

    if not user_info:
        return jsonify({'message': '请求错误'}), 415

    success = UploadUserIdentificationService.upload(user_info)

    if success:
        return jsonify({'message': '成功上传用户信息！'}), 200
    else:
        return jsonify({'message': '上传用户信息失败！'}), 500
