from app import socketio


class InteractWithNanoService:
    @staticmethod
    def get_face_image_from_nano_service(signal: int):
        # 使用 socketio 来与 Nano 服务进行通信
        # 使用在init中定义好的事件处理函数传送信号量
        socketio.emit('message', signal)
        response = None

        @socketio.on('response')
        def handle_response(data):
            # 使用 nonlocal 关键字来声明这个变量是来自外部函数的变量
            nonlocal response
            response = data

        # 这里可以加入一些超时机制，以防止长时间等待响应
        socketio.sleep(5)

        return response
