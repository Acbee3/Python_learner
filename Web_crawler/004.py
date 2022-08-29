import requests
import csv
from bs4 import BeautifulSoup

list_url = 'https://www.xiachufang.com/explore/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
list_res = requests.get(list_url, headers=header)
list_res.encoding = 'utf-8'
print(list_res.status_code)
bs = BeautifulSoup(list_res.text, 'html.parser')
food_list_tag = bs.find(class_='normal-recipe-list').find_all('li')
food_msg = []
for food_tag in food_list_tag:
    dict = {}
    dict['名称'] = food_tag.find(class_='name').find('a').text.strip()
    dict['链接'] = ''.join(['https://www.xiachufang.com/', food_tag.find(class_='name').find('a')['href']])
    list = []
    for item_1 in food_tag.find(class_='ing ellipsis').find_all('span'):
        list.append(item_1.text.strip())
    for item_2 in food_tag.find(class_='ing ellipsis').find_all('a'):
        list.append(item_2.text.strip())
    dict['食材'] = '、'.join(list)
    food_msg.append(dict)
print(food_msg)

with open('下厨房.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['名称', '链接', '食材'])
    writer.writeheader()
    writer.writerows(food_msg)