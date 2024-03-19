from app.models.users import Users
from app import db

class ModifyUserInformationService:
    @staticmethod
    def modify(user_id, url_dict):
        # 查询对应用户记录
        user = Users.query.filter(Users.id == user_id, Users.is_valid == 1).first()
        # 如果用户存在，更新用户信息并保存到数据库
        if user:
            # 遍历传来的URL列表，筛选需要更新的字段并更新到数据库中
            for key, value in url_dict.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            db.session.commit()
            return True
        else:
            return False
    @staticmethod
    def delete(user_id):
        user = Users.query.filter(Users.id == user_id, Users.is_valid == 1).first()
        if user:
            user.is_valid = 0
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def find_by_id(user_ids):
        users = Users.query.filter(Users.id.in_(user_ids),Users.is_valid==1).all()
        invalid_users = Users.query.filter(Users.id.in_(user_ids),Users.is_valid==0).all()
        if invalid_users:
            valid_users_info = [{
            'id': user.id,
            'username': user.username,
            'fingerprint_image_url': user.fingerprint_image_url,
            'face_image_url': user.face_image_url,
            'voice_print_url': user.voice_print_url,
            'gait_near_url': user.gait_near_url,
            'gait_far_url': user.gait_far_url
            } for user in users]
            invalid_user_ids = [user.id for user in invalid_users]
            return valid_users_info, invalid_user_ids
        else:
            users_info=[{
            'id' : user.id,
            'username' : user.username,
            'fingerprint_image_url' : user.fingerprint_image_url,
            'face_image_url' : user.face_image_url,
            'voice_print_url' : user.voice_print_url,
            'gait_near_url' : user.gait_near_url,
            'gait_far_url' : user.gait_far_url
        }for user in users]
        return users_info
    
    @staticmethod
    def find_by_name(username):
        users = Users.query.filter(Users.username == username, Users.is_valid==1).all()

        users_info = [{
            'id' : user.id,
            'username' : user.username,
            'fingerprint_image_url' : user.fingerprint_image_url,
            'face_image_url' : user.face_image_url,
            'voice_print_url' : user.voice_print_url,
            'gait_near_url' : user.gait_near_url,
            'gait_far_url' : user.gait_far_url
        }for user in users]
        return users_info