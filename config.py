import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/24jsjds'
    # 不追踪对象的修改并发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT 配置
    JWT_SECRET_KEY = 'punkginger'  # 设置密钥，用于签名 Token
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 设置访问令牌的过期时间（秒）

    # 上传目录
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'loacl_server', 'upload')  # 上传文件的目录

    # ws超时重传时间设置
    WS_TIMEOUT_SECOND = 7
