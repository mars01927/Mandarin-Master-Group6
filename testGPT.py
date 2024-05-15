import requests
import json
#修改成自己的api key和secret key
API_KEY = "8JX9tTtoyKv0KF8NEs2bE0Do"
SECRET_KEY = "PVKSXaSLrvRqdWmYGkPwm5vNEup4bpEj"
 
 
def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "现在请你扮演一个语言学习软件的评分助手，请评估这两个句子之间语音相似的百分比。请注意，你只需要提供一个数字。只提供数字。'你吃饭了吗' 和 '你吃了吗'。"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
 
    response = requests.request("POST", url, headers=headers, data=payload)
 
    print(response.text)
 
 
def get_access_token():

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 
 
if __name__ == '__main__':
    main()