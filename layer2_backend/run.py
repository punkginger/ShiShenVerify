from flask import Flask
import config

app = Flask(__name__)


@app.route('/api/data')
def get_data():
    # 在这里可以返回一些数据给前端，比如 JSON 数据
    data = {'message': 'Hello from Flask!'}
    return data


if __name__ == '__main__':
    ip = config.Config.IP_ADDRESS
    port = config.Config.PORT
    app.run(host=ip, debug=True, port=port)
