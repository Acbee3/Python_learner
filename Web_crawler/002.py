import csv
from dataclasses import fields
import requests
from bs4 import BeautifulSoup

# (headers 的相关知识会在下节课详细讲解，可暂时忽略此处代码)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

url = 'https://www.boohee.com/food/group/{}?page={}'

list = []

for group in range(1, 4):
    for page in range(1, 4):
        res = requests.get(url.format(group, page), headers=headers)
        url_tmp = (url.format(group, page))
        if res.status_code != 200:
            raise
        bs = BeautifulSoup(res.text, 'html.parser')
        classification = bs.find('div', class_='widget-food-list pull-right')
        group_name = classification.find('h3').text.strip()
        infos = classification.find_all('div', class_='text-box pull-left')
        for info in infos:
            item_name = info.find('a')['title'].strip()
            item_link = ''.join(['https://www.boohee.com/', info.find('a')['href']])
            item_calorie = info.find('p').text[3:]
        dict = {
            '类别': group_name,
            '食物': item_name,
            '热量': item_calorie,
            '链接': item_link
        }
        list.append(dict)
        
with open('./Python/Web_crawler/food.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['类别', '食物', '热量', '链接'])
    writer.writeheader()
    writer.writerows(list)
    