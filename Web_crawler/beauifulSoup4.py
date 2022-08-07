from bs4 import BeautifulSoup
import requests

url = "https://bbs.white-plus.net/"

res = requests.get(url)

print(res.status_code)
res.encoding = 'utf-8'
print(res.text)