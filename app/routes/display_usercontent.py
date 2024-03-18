from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.display_usercontent_service import DisplayUserContentService

index_blueprint = Blueprint('index_blueprint', __name__)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401

@index_blueprint.route('/index', methods=['GET'])
@jwt_required()  # 使用 JWT 鉴权保护路由
def get_index():
    # 获取页码，默认为第一页
    page = int(request.args.get('page',1))

    # 调用用户服务获取用户信息
    users_info = DisplayUserContentService.get_users(page)

    if isinstance(users_info, str):
        return jsonify(message=users_info),404
    else:
        return jsonify(users_info),200
