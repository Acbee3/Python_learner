import csv
from bs4 import BeautifulSoup
import requests

page_number = 1
info_list = []
while page_number < 4:
    url = "https://wp.forchange.cn/resources/page/" + str(page_number)
    
    try:
        res = requests.get(url)
        if res.status_code == 200:
            res.encoding = 'utf-8'
            bs = BeautifulSoup(res.text, 'html.parser')
            bookname_list = bs.find_all('a', class_='post-title')
            for book_info in bookname_list:
                info_dict = {}
                bookname = book_info.text
                booklink = book_info['href']
                info_dict['书名'] = bookname
                bookres = requests.get(booklink)
                bookres.encoding = 'utf-8'
                bs_book = BeautifulSoup(bookres.text, 'html.parser').find('div', class_='res-attrs')
                info_tag = bs_book.find_all('dl')
                
                for info in info_tag:
                    info_dict[info.find('dt').text[:-2]] = info.find('dd').text
                
                info_list.append(info_dict)
                
        page_number += 1
        
    except:
        print('出错啦')
with open('./Python/Web_crawler/book.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['书名', '作者', '出版社', 'ISBN', '页数', '出版年', '定价']
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(info_list)