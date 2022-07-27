# 作者：小甲鱼
# 来源：https://fishc.com.cn/thread-150254-1-1.html
# 本代码著作权归作者所有，禁止商业或非商业转载，仅供个人学习使用，违者必究！
# Copyright (c) 2020 fishc.com.cn All rights reserved

i = 1
FIND = False

while i < 1000:
    if i % 7 == 0 and i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5:
        FIND = True
        break
    else:
        i = i + 1

if FIND == True:
    print('阶梯数是：', i)
else:
    print('在程序限定的范围内找不到答案！')
