s = input("请输入一个字符串：")
   
res = []
for each in s:
    if res and res[-1].lower() == each.lower() and res[-1] != each:
        res.pop()
    else:
        res.append(each)
   
for each in res:
    print(each, end='')