from packs_from_nano import layer1_nano_V2

'''
nano部分：
    class layer1()
        run(self, mode)
            # mode=1:带活体检测的人脸识别
            # mode=2:指纹识别
            # mode=3:人脸登记
            # mode=4:指纹登记
'''


class VerifyLayersService:

    @staticmethod
    def verify_layer1_service(mode):
        verify = layer1_nano_V2.layer1()
        result = verify.run(mode)
        return result

