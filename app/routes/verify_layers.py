from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.verify_layers_service import VerifyLayersService

verify_layers_blueprint = Blueprint('verify_layers_blueprint', __name__)


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401


# 第一层识别：人脸 指纹 在本地（nano上实现）
# 第二层识别：声纹 步态 （树莓派）
'''
nano部分：
    class layer1()
        run(self, mode)
            # mode=1:带活体检测的人脸识别
            # mode=2:指纹识别
            # mode=3:人脸登记
            # mode=4:指纹登记
'''


@verify_layers_blueprint.route('/api/getFaceImage', methods=['GET'])
@jwt_required()
def get_face_image():
    # 前端访问此接口时，由后端向nano传送一个信号量
    mode = 1
    try:
        result = VerifyLayersService.verify_layer1_service(mode)
        if result is None:
            return jsonify(message='后台交互失败'), 500
        else:
            return jsonify(result), 200
    except Exception as e:
        # 处理与 Nano 服务通信的异常
        return jsonify(message='与 Nano 服务通信失败'), 504


@verify_layers_blueprint.route('/api/getFingerprint', methods=['GET'])
@jwt_required()
def get_fingerprint():
    mode = 2
    try:
        result = VerifyLayersService.verify_layer1_service(mode)
        if result is None:
            return jsonify(message='后台交互失败'), 500
        else:
            return jsonify(result), 200
    except Exception as e:
        # 处理与 Nano 服务通信的异常
        return jsonify(message='与 Nano 服务通信失败'), 504
