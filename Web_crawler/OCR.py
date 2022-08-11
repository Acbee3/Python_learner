import requests
import time

login_data = {
    'lgt': 0,
    'pwuser': 'pipilili33',
    'pwpwd': 'pandorahatu',
    'gdcode': 0000,
    'hideid': 0,
    'forward': "//bbs.white-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html",
    'jumpurl': "//bbs.white-plus.net/plugin.php?H_name-tasks-actions-newtasks.html.html",
    'step': 2,
    'cktime': 31536000
}
login_url = "https://bbs.white-plus.net/login.php?"

gdcode_url = "https://bbs.white-plus.net/ck.php?nowtime={}".format(round(time.time() * 1000))

task_daily_url = "https://bbs.white-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job&cid=15&nowtime={}&verify=803e93f6".format(round(time.time() * 1000))
reward_daily_url = "https://bbs.white-plus.net/plugin.php?H_name=tasks&action=ajax&actions=job2&cid=15&nowtime={}&verify=803e93f6".format(round(time.time() * 1000))


res = requests.get(gdcode_url)
print(res.content)