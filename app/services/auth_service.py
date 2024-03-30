from flask_jwt_extended import create_access_token
from app.models import Admin


class AuthService:
    @staticmethod
    def login(username, password):
        # 查询数据库中是否存在匹配的管理员
        admin = Admin.query.filter_by(username=username).first()

        # 检查用户名和密码是否匹配
        if admin and admin.password == password:
            # 生成并返回访问令牌(Token)
            access_token = create_access_token(identity=admin.id)
            return {'access_token': access_token, 'message': '登录成功'}, 200
        else:
            return {'message': '用户名或密码错误'}, 401
