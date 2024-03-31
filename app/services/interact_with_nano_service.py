from app import socketio
import threading
from config import Config

'''
nano部分：
    class layer1()
        run(self, mode)
            # mode=1:带活体检测的人脸识别
            # mode=2:指纹识别
            # mode=3:人脸登记
            # mode=4:指纹登记
'''


class InteractWithNanoService:
    @staticmethod
    def get_face_image_from_nano_service(mode):

        pass

    @staticmethod
    def get_fingerprint_from_nano_service(mode):
        pass
