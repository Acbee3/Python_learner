import requests

url = "https://aip.baidubce.com/oauth/2.0/token"

data = {
    'grant_type': 'client_credentials',
    'client_id': 'y5CmgnfZp6aeZKiu0Bm2ZhZw',
    'client_secret': '2QV51vk1M7r6POqEpBGTxDwCDjBxKuID'
}

res = requests.post(url, data=data)
sk = str(res.json()['access_token'])
print(res.json())

