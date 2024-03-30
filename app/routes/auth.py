from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    response, status_code = AuthService.login(username, password)
    return jsonify(response), status_code
