# encoding:utf-8
import base64
import requests
'''
通用文字识别（高精度版）
'''
url = "https://aip.baidubce.com/oauth/2.0/token"

data = {
    'grant_type': 'client_credentials',
    'client_id': 'y5CmgnfZp6aeZKiu0Bm2ZhZw',
    'client_secret': '2QV51vk1M7r6POqEpBGTxDwCDjBxKuID'
}

res = requests.post(url, data=data)
sk = str(res.json()['access_token'])
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('D:/Code/Python/Web_crawler/a.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = sk
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())