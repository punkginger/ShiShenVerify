from flask import Flask, jsonify, request
import threading, uuid
import config
# 引入二层识别模块
import sys
sys.path.append('./demo/libs')
from OpenGait.demo.libs import layer2_main

app = Flask(__name__)
results = {}

@app.route('/api/verifyLayer2', methods=['GET'])
def get_voice():
    task_id = str(uuid.uuid4())
    thread = threading.Thread(target=layer2_verify, args=(task_id,))
    thread.start()
    return jsonify({'task_id': task_id,'message': "正在识别中"}), 202
    

def layer2_verify(task_id):
    verify = layer2_main.layer2()
    result = jsonify(verify.layer2_start())
    results[task_id] = result


# 需要客户端不断轮询该接口获取结果
@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    if task_id in results:
        return jsonify({'result': results.pop(task_id)})
    else:
        return jsonify({'message': '处理中'}), 202


if __name__ == '__main__':
    # 引用示例
    run_layer2 = layer2_main.layer2()
    run_layer2.layer2_start()

    ip = config.Config.IP_ADDRESS
    port = config.Config.PORT
    app.run(host=ip, debug=True, port=port)
