import requests
from bs4 import BeautifulSoup

password = 'UFVkBHAD4sZoGTR2'
username = 'liuchaoacbee3@163.com'
url_login = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
url_comment = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_01/'
url_post = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'

# 获取最早的评论
comment_res = requests.get(url_comment)
newest_comment_text = BeautifulSoup(comment_res.text, 'html.parser').find(id='div-comment-93').find('p').text.strip()
print(newest_comment_text)

# 登录网页
data_login = {
    'log': 'liuchaoacbee3@163.com',
    'pwd': 'UFVkBHAD4sZoGTR2',
    'rememberme': 'forever',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': 1
}

login_res = requests.post(url_login, data=data_login)
cookies = login_res.cookies

# 发表评论
comment = input('发表你的评论：')
data_comment = {
    'comment': comment,
    'submit': '发表评论',
    'comment_post_ID': 13,
    'comment_parent': 0
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
login_res = requests.post(url_post, data=data_comment, cookies=cookies, headers=header)
print(login_res)
