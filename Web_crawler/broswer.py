from re import T
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image, ImageFilter
import time
import requests

import twochptcha

hash = {
    'pipilili33': '9cbcef9e',
    'pill2': '803e93f6'
}

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

url = "https://bbs.white-plus.net/ck.php?nowtime={}"

task_daily_url = "https://bbs.white-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=15&nowtime={}&verify={}".format(round(time.time() * 1000), hash['pipilili33'])
reward_daily_url = "https://bbs.white-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=15&nowtime={}&verify={}".format(round(time.time() * 1000), hash['pipilili33'])
            
service = Service(executable_path="d:/chromedriver")
opts = Options()
opts.headless = True
driver = webdriver.Chrome(service=service, options=opts)
# # 打开网页
# 打开url网页 比如 driver.get("http://www.baidu.com")
driver.get("https://bbs.white-plus.net/plugin.php?H_name-tasks.html")
driver.maximize_window()
driver.implicitly_wait(7)
# for cookie in cookie_list:
#     driver.add_cookie(cookie)
    
# driver.refresh()

name_user = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div[2]/table/tbody/tr[2]/th/form/fieldset/table/tbody/tr[1]/td[2]/input')
pwd_input = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div[2]/table/tbody/tr[2]/th/form/fieldset/table/tbody/tr[2]/td[2]/input')
gdcode_input = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div[2]/table/tbody/tr[2]/th/form/fieldset/table/tbody/tr[3]/td[2]/input')
name_user.send_keys('pipilili33')
pwd_input.send_keys('pandorahatu')
gdcode_input.click()
WebDriverWait(driver, timeout=10).until(lambda a : driver.find_element(by=By.CSS_SELECTOR, value="img[align=absmiddle]"))
code_image = driver.find_element(by=By.CSS_SELECTOR, value="img[align=absmiddle]")
time.sleep(5)
gdImage = code_image.screenshot_as_png
imageURL = "D:\Code\Python\Web_crawler\\a.jpg"
with open(imageURL, 'wb') as f:
        f.write(gdImage)
code = str(twochptcha.image_to_string())
time.sleep(10)
print(code)
gdcode_input.send_keys(code)
login_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div[2]/table/tbody/tr[2]/th/form/center/input')
login_button.click()
time.sleep(5)
cookie_list = driver.get_cookies()
print(cookie_list)

# 创建储存 cookie 的空字符
cookies = ''

# 遍历 cookie 列表，取出目标 cookie 信息
for cookie in cookie_list:
    cookies += '{}={};'.format(cookie['name'], cookie['value'])
# 设置请求头
header = {
    'Cookie': cookies,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
driver.quit()

task_res = requests.get(task_daily_url, headers=header)
print(task_res.text)
time.sleep(5)
reward_res = requests.get(reward_daily_url, headers=header)
print(reward_res.text)
