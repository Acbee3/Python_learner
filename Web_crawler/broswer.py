from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image, ImageFilter
import pytesseract
import time
import requests

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

url = "https://bbs.white-plus.net/ck.php?nowtime={}"

def create_image(link = ''):
    if link != '':
        res = requests.get(link, headers=headers)
        print(link)
    else:
        now = int(round(time.time())*1000)
        res = requests.get(url.format(now), headers=headers)
        
    with open('a.jpg', 'wb') as f:
        f.write(res.content)
    global code    
    code = input("输入验证码：\n")
    if code == 'no':
        create_image()
            
service = Service(executable_path="d:/chromedriver")
driver = webdriver.Chrome(service=service)
# # 打开网页
# 打开url网页 比如 driver.get("http://www.baidu.com")
driver.get("https://bbs.white-plus.net/plugin.php?H_name-tasks.html")
# driver.get("http://www.baidu.com") # 打开url网页 比如 driver.get("http://www.baidu.com")
# print(driver)
driver.implicitly_wait(7)

# for cookie in cookie_list:
#     driver.add_cookie(cookie)
    
# driver.refresh()

name_user = driver.find_element(by=By.ID, value="pwuser")
pwd_input = driver.find_element(by=By.NAME, value="pwpwd")
gdcode_input = driver.find_element(by=By.NAME, value="gdcode")
submit_btn = driver.find_element(by=By.XPATH, value='//*[@id="user_info"]/div/div/div/form/div[1]/div/input[3]')
balnk_click = driver.find_element(by=By.XPATH, value='//*[@id="shortcutname"]')
name_user.send_keys('')
pwd_input.send_keys('')
gdcode_input.click()
# driver.implicitly_wait(1)
# code_image = driver.find_element(by=By.CSS_SELECTOR, value="img[align=absmiddle]")
# code_image_src = code_image.get_attribute('src')


create_image()
# code = input("验证码：\n")
# gdcode_input.send_keys(code)
# balnk_click.click()
# submit_btn.click()

task_days = driver.find_element(by=By.XPATH, value='//*[@id="p_15"]/a')
task_days and task_days.click()

driver.implicitly_wait(1)
pending_task = driver.find_element(by=By.XPATH, value='//*[@id="main"]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td/a')
driver.implicitly_wait(4)
rewards_days = driver.find_element(by=By.XPATH, value='//*[@id="both_15"]/a')
rewards_days and rewards_days.click()
# driver.switch_to.new_window('tab')
# driver.get(code_image_src)
# str = identify_image(code_image_src)
# print(str)
print(driver.current_window_handle)
# driver.close()


