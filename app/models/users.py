from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fingerprint_image_url = db.Column(db.String(128))
    face_image_url = db.Column(db.String(128))
    voice_print_url = db.Column(db.String(128))
    gait_near_url = db.Column(db.String(128))
    gait_far_url = db.Column(db.String(128))
    is_valid = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<User {self.username}>'
