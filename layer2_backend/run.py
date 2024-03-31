from flask import Flask, jsonify
import config
import asyncio
# import apack used by layer2

app = Flask(__name__)


@app.route('/api/getVoice', methods=['GET'])
async def get_voice():
    result = await asyncio.sleep(5)  # analog
    return jsonify(result)

@app.route('/api/getGait', methods=['GET'])
async def get_gait():
    result = await asyncio.sleep(5)
    return jsonify(result)

if __name__ == '__main__':
    ip = config.Config.IP_ADDRESS
    port = config.Config.PORT
    app.run(host=ip, debug=True, port=port)
