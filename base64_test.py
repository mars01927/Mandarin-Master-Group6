import requests
import base64
import time
import hashlib
import hmac

# 设置请求地址
url = "https://fanyi-api.baidu.com/api/trans/v2/voicetrans"

# 设置请求头
headers = {
    "Content-Type": "application/json",
    "X-Appid": "20240508002045408",  # 从管理控制台中获取
}

# 设置请求体
from_language = "yue"
to_language = "zh"
format = "pcm"
voice_file_path = "njsmmz.pcm"

# 读取音频文件并进行base64编码
with open(voice_file_path, "rb") as audio_file:
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

# 发送POST请求
response = requests.post(url, json=payload, headers=headers)

# 处理响应
if response.status_code == 200:
    print("Request successful!")
    print("Response:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
