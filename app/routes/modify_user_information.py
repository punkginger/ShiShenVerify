from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app import jwt
from app.services.modify_user_information_service import ModifyUserInformationService

modify_user_information_blueprint = Blueprint('modify_user_information_blueprint',__name__)

@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return jsonify(message='请先登录'), 401

@modify_user_information_blueprint.route('/modify',methods=['POST'])
@jwt_required()
def modify():
    user_id = request.json.get('userId')
    file_urls = request.json.get('fileUrls')

    result = ModifyUserInformationService.modify(user_id,file_urls)
    if result:
        return jsonify(message='用户信息修改成功'), 200
    else:
        return jsonify(message='用户信息修改失败'), 400

@modify_user_information_blueprint.route('/delete',methods=['POST'])
@jwt_required()
def delete():
    user_id = request.json.get('userId')

    result = ModifyUserInformationService.delete(user_id)
    if result:
        return jsonify(message='用户信息删除成功'), 200
    else:
        return jsonify(message='用户信息删除失败'), 400

@modify_user_information_blueprint.route('/findById',methods=['GET'])
@jwt_required()
def find_by_id():
    # 获取请求中的用户ID列表
    user_ids = request.json.get('userIds', [])
    # 调用服务方法查找用户信息
    users_info = ModifyUserInformationService.find_by_id(user_ids)

    if user_info:
        return jsonify(users_info),200
    else:
        return jsonify(message='用户不存在'),404

@modify_user_information_blueprint.route('/findByName',methods=['GET'])
@jwt_required()
def find_by_name():
    username = request.json.get('username')
    users_info = ModifyUserInformationService.find_by_name(username)

    if users_info:
        return jsonify(users_info),200
    else:
        return jsonify(message='用户不存在'),404