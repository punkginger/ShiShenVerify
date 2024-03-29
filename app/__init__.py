from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config.from_pyfile('../config.py')
app.config.from_object(Config)

socketio = SocketIO(app)

db = SQLAlchemy(app)

jwt = JWTManager(app)

# 蓝图注册
from app.routes.auth import auth_blueprint
from app.routes.display_usercontent import index_blueprint
from app.routes.upload_user_identification import upload_user_identification_blueprint
from app.routes.upload_file import upload_file_blueprint
from app.routes.modify_user_information import modify_user_information_blueprint
from app.routes.interact_with_nano import interact_with_nano_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(index_blueprint)
app.register_blueprint(upload_user_identification_blueprint)
app.register_blueprint(upload_file_blueprint)
app.register_blueprint(modify_user_information_blueprint)
app.register_blueprint(interact_with_nano_blueprint)

# 模型注册
from app.models.admin import Admin
from app.models.users import Users


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('message')
def handle_message(data):
    print(f"Received message from Nano: {data}")

    # 在这里调用与 Nano 通信的业务逻辑，这里用一个简单的示例代替
    result = {"integer_value": 42}

    # 将结果返回给客户端
    emit('message', result)
