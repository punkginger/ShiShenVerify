from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.upload_file_service import UploadFileService

upload_file_blueprint = Blueprint('upload_file_blueprint', __name__)


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401


@upload_file_blueprint.route('/api/file', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return jsonify(message='没有文件，请上传文件'), 400

    # 选择为空的话也会上传一个空文件
    file = request.files['file']
    if file.filename == '':
        return jsonify(message='未选择文件'), 422

    uploaded_file_url = UploadFileService.upload(file)

    if uploaded_file_url:
        return jsonify(message='文件上传成功', url=uploaded_file_url), 200
    else:
        return jsonify(message='上传文件失败'), 500
