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
    if request.json:
        user_id = request.json.get('userId')
        file_urls = request.json.get('fileUrls')
        file_needs_mod = request.json.get("fileNeedsMod")
    else:
        return jsonify(message='请求信息错误'),415

    url_dict={}
    for k,v in zip(file_needs_mod,file_urls):
        url_dict[k]=v
    result = ModifyUserInformationService.modify(user_id,url_dict)
    if result:
        return jsonify(message='用户信息修改成功'), 200
    else:
        return jsonify(message='用户信息修改失败'), 400

@modify_user_information_blueprint.route('/delete',methods=['POST'])
@jwt_required()
def delete():
    if request.json:
        user_id = request.json.get('userId')
    else:
        return jsonify(message='请求信息错误'),415


    result = ModifyUserInformationService.delete(user_id)
    if result:
        return jsonify(message='用户信息删除成功'), 200
    else:
        return jsonify(message='用户信息删除失败'), 400

@modify_user_information_blueprint.route('/findById',methods=['GET'])
@jwt_required()
def find_by_id():
    # 获取请求中的用户ID列表
    if request.args:
        user_ids = request.args.getlist('userIds')
    else:
        return jsonify(message='请求信息错误'),415
    # 调用服务方法查找用户信息
    result = ModifyUserInformationService.find_by_id(user_ids)

    if not result:
        return jsonify(message='用户不存在'),404
    elif isinstance(result, tuple):
        valid_users_info, invalid_user_ids = result
        return jsonify({
            'valid_users_info': valid_users_info,
            'invalid_user_ids': invalid_user_ids
        }),200
    else:
        # 如果服务只返回了有效用户信息，则直接返回
        return jsonify(valid_users_info = result),200


@modify_user_information_blueprint.route('/findByName',methods=['GET'])
@jwt_required()
def find_by_name():
    if request.args:
        username = request.args.get('username')
    else:
        return jsonify(message='请求信息错误'),415
    users_info = ModifyUserInformationService.find_by_name(username)

    if users_info:
        return jsonify(users_info),200
    else:
        return jsonify(message='用户不存在'),404