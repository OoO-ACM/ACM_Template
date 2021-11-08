import requests

path = '1.jpg'
url = 'http://xmbot.net:10002/up_photo'
res = requests.post(url=url, files={'photo': open(path, 'rb')})
print(res.text)

