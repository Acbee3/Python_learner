import urllib.request
res = urllib.request.urlopen("https://ilovefishc.com/")
html = res.read()
print(html)