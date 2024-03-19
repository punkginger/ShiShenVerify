from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.display_usercontent_service import DisplayUserContentService
#import math

index_blueprint = Blueprint('index_blueprint', __name__)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401

@index_blueprint.route('/index', methods=['GET'])
@jwt_required()  # 使用 JWT 鉴权保护路由
def get_index():
    # 获取页码，默认为第一页
    page = int(request.args.get('page',1))
    per_page = 10
    # 调用用户服务获取用户信息
    users_info, toal_valid_users = DisplayUserContentService.get_users(page,per_page)

    if isinstance(users_info, str):
        return jsonify(message=users_info),404
    else:
        #toal_pages = math.ceil(toal_valid_users / per_page)
        return jsonify({
            'users_info': users_info,
            'total_valid_users': toal_valid_users
            }),200
