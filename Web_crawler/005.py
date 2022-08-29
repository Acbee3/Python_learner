import requests
from bs4 import BeautifulSoup
page_url = 'https://wp.forchange.cn/resources/page/{}/'

list = []

for page in range(1, 4):
    print(page_url.format(page))
    res = requests.get(page_url.format(page))
    res.encoding = 'utf-8'
    print(res.status_code)
    bs = BeautifulSoup(res.text, 'html.parser')
    item_tag = bs.find_all('article', class_='post')
    for item in item_tag:
        dict = {}
        dict['名称'] = item.find('img')['alt']
        dict['封面链接'] = item.find('img')['data-src']
        list.append(dict)
        
print(list)
for book in list:
    obj = requests.get(book['封面链接'])
    with open('%s.jpg' % book['名称'], 'wb') as f:
        f.write(obj.content)