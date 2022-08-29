import time
import requests
import re
import csv

list = ['002709', '002594', '603185', '002460', '601633', '002466', '000821', '600703', '600563', '002240', '159949', '003022', '000858', '603799', '000831', '600111', '002518', '600760', '600862', '002297', '603005', '600338', '600406', '600711', '159863', '002202', '603158', '000799', '002487', '600021', '002639', '600362', '601919', '603986', '002612', '601865']
now_time = round(time.time() * 1000)
url = 'https://xueqiu.com/query/v1/search/web/stock.json?q={}&size=3&page=1'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'acw_tc=276077b716617814423877707ec19472a4cc09fdc56d60ef63dbf230f163ab; xq_a_token=28ed0fb1c0734b3e85f9e93b8478033dbc11c856; xqat=28ed0fb1c0734b3e85f9e93b8478033dbc11c856; xq_r_token=bf8193ec3b71dee51579211fc4994d03f17c64ac; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MzExMzIyMSwiY3RtIjoxNjYxNzgxNDI1NjU4LCJjaWQiOiJkOWQwbjRBWnVwIn0.bAkdH_QhuQoKXvRdsYvPlXzM7FYcZ7TFSO5j4uljVIFo6H0TZhQHkKo2SFSM-9luCCkWBjnb08ug0DYMqVYFq_JxEyTd9a4yw4zfH_PlmniZE8iCBjnnRIc0U5M4bxS0ZLtyN2MPcVBdscV7cP_RBZRKSOgTJcWniyPSzLX9TbI3rtO1FGTMFSQ61DyC81XiKuZQ-Bl3c_I8CAXaEvviYw07gVAbAnEDsCWId1G9zcfBCoJOcvEjBZdKz12X-0u-knqimx5ledLFp05Upi7pBngu6S2BfFvILS_7qnhMXiXS1NEP6QPGyUl0OC2oohol9kIYXMiTFrvkNw5QjpmsvQ; u=641661781442395; device_id=7742885f34ef6038a0cc3696605f154e; Hm_lvt_1db88642e346389874251b5a1eded6e3=1661781447; s=cz12n3ruux; __utma=1.332590893.1661782023.1661782023.1661782023.1; __utmc=1; __utmz=1.1661782023.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.5.10.1661782023; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1661782981'
}
data_list = []
pattern = re.compile('\D{2}\d{6}')
for code in list:
    res = requests.get(url.format(code), headers=header)
    res_list = res.json()['list']
    for index, data in enumerate(res_list):
        dict = {}
        if pattern.match(data['code']):
            dict['code'] = data['code'] or ''
            dict['name'] = data['name'] or ''
            dict['current'] = data['current'] or ''
            # dict['indName'] = data['indName'] or ''
            dict['percentage'] = data['percentage'] or ''
        else:
            print(data)
        data_list.append(dict)
print(data_list)

with open('D:/Code/Python/Web_crawler/代码.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['code', 'name', 'current', 'percentage'])
    writer.writeheader()
    writer.writerows(data_list)