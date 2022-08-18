from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path="C:\edgedriver_win64\msedgedriver.exe")
options = EdgeOptions()
# options.headless = True
driver = webdriver.Edge(service=service, options=options)

def document_initialised(driver):
    return driver.find_element(by=By.XPATH, value='//*[@id="loginform"]/div[1]/input')

driver.get('http://music.facode.cn/index.php/Home/Index/login.html')
WebDriverWait(driver, timeout=10).until(document_initialised)
name_input = driver.find_element(by=By.XPATH, value='//*[@id="loginform"]/div[1]/input')
name_input.send_keys('')
driver.implicitly_wait(1)
password_input = driver.find_element(by=By.XPATH, value='//*[@id="loginform"]/div[2]/input')
password_input.send_keys('')
# 打印网页的源代码
print(driver.page_source)

# 关闭浏览器
driver.quit()
