import websocket
import json


class InteractWithNanoService:
    @staticmethod
    def get_face_image_from_nano_service(signal: int):
        nano_address = "ws://127.0.0.1:5000"  # 例子
        ws = websocket.create_connection(nano_address)
        ws.send(json.dumps(signal))
        response = ws.recv()
        ws.close()
        result = json.loads(response)
        return result
