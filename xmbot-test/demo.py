import requests
import random
import json

# 请求网址
requestUrl = "https://xmbot.net/sync/userMessage"
# 用户Id
userId = "testUserId" + str(random.randint(0,9999))
# 消息Id
msgId = str(random.randint(0,999999999))
# 图片url
imgUrl = "http://xmbot.net:10002/download/pic.jpg"
# 问题文本
ques = "What is she doing?"

# 请求体
payload = json.dumps({
    "openid": userId,
    "submit_id": msgId,
    "url": imgUrl,
    "problem": ques,
    "answer":""
    })

r = requests.post(requestUrl, data= payload)
print(r.text)
