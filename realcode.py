from flask import Flask, request, jsonify
import base64
import time
import hashlib
import hmac
import requests

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # 保存音频文件到本地
    audio_file_path = "uploaded_audio.pcm"  # 保存为 PCM 文件
    file.save(audio_file_path)

    # 准备发送至百度翻译的请求
    url = "https://fanyi-api.baidu.com/api/trans/v2/voicetrans"
    headers = {
        "Content-Type": "application/json",
        "X-Appid": "20240508002045408",  # 从管理控制台中获取
    }
    from_language = "yue"
    to_language = "zh"
    format = "pcm"  # 设置为 PCM 格式

    # 读取音频文件并进行base64编码
    with open(audio_file_path, "rb") as audio_file:
        voice_binary_data = audio_file.read()
        voice_base64 = base64.b64encode(voice_binary_data).decode("utf-8")

    # 构建请求体
    payload = {
        "from": from_language,
        "to": to_language,
        "format": format,
        "voice": voice_base64
    }

    # 设置X-Timestamp参数
    X_Timestamp = str(int(time.time()))
    headers["X-Timestamp"] = X_Timestamp

    # 构建请求签名X-Sign
    concat_str = headers["X-Appid"] + X_Timestamp + payload["voice"]
    secret_key = "ITW006BC5yVWRL93P4pX"  # 从管理控制台中获取
    signature = hmac.new(secret_key.encode("utf-8"), concat_str.encode("utf-8"), hashlib.sha256).digest()
    X_Sign = base64.b64encode(signature).decode("utf-8")
    headers["X-Sign"] = X_Sign

    # 发送 POST 请求至百度翻译
    response = requests.post(url, json=payload, headers=headers)

    # 处理响应
    if response.status_code == 200:
        translation_result = response.json()
        # 提取目标字段的值
        target_text = translation_result.get("data", {}).get("target", "")
        if target_text.endswith('，'):
            target_text = target_text[:-1]
        return target_text


    else:
        return 'Request failed with status code: ' + str(response.status_code)

if __name__ == '__main__':
    app.run(debug=True)
