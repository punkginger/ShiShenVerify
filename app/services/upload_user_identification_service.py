from app.models.users import Users
from app import db

class UploadUserIdentificationService:
    @staticmethod
    def upload(user_info):
        # 从 JSON 数据中提取用户信息
        username = user_info.get('username')
        fingerprint_image_url = user_info.get('fingerprint_image_url')
        face_image_url = user_info.get('face_image_url')
        voice_print_url = user_info.get('voice_print_url')
        gait_near_url = user_info.get('gait_near_url')
        gait_far_url = user_info.get('gait_far_url')

        # 检查是否提供了所需的用户信息
        if not (username and fingerprint_image_url and face_image_url and voice_print_url and gait_near_url and gait_far_url):
            return False

        # 创建新的用户对象并添加到数据库中
        user = Users()
        user.username=username,
        user.fingerprint_image_url=fingerprint_image_url,
        user.face_image_url=face_image_url,
        user.voice_print_url=voice_print_url,
        user.gait_near_url=gait_near_url,
        user.gait_far_url=gait_far_url

        # 添加到数据库并提交更改
        db.session.add(user)
        db.session.commit()

        return True