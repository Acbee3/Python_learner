import os
import requests
# key_word = input('请输入要搜索的内容：')
key_word = 'sky'
pic_url = 'https://unsplash.com/napi/search/photos?query={}&per_page=20&page={}&xp=unsplash-plus-2%3AControl'
page = 2

res = requests.get(pic_url.format(key_word, 2))
print(res.status_code)
data = res.json()
image_info_list = data['results']
for img in image_info_list:
    link = img.get('urls').get('thumb')
    print(link)
    