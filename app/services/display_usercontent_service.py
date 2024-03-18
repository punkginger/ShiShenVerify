from app.models.users import Users

class DisplayUserContentService:
    @staticmethod
    def get_users(page):
        # 每页显示的记录数
        per_page = 8

        # 计算偏移量
        offset = (page - 1) * per_page

        # 查询用户信息
        users = Users.query.with_entities(Users.id, Users.username, Users.fingerprint_image_url, Users.voice_print_url, Users.voice_print_url, Users.gait_near_url, Users.gait_far_url).filter(Users.is_valid==1).offset(offset).limit(per_page).all()
        
        if not users:
            return '没有用户信息！'
        
        # 格式化查询结果
        formatted_users = [{
            'id': user.id,
            'username': user.username,
            'fingerprint_image_url': user.fingerprint_image_url,
            'face_image_url': user.face_image_url,
            'voice_print_url': user.voice_url,
            'gait_near_url': user.gait_near_url,
            'gait_far_url': user.gait_far_url
        } for user in users]

        return formatted_users
