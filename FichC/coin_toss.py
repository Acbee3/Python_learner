import random

counts = int(input("请输入抛硬币的次数："))
i = 0
count_0 = 0
count_1 = 0
print("开始抛硬币实验：")
while i < counts:
    num = random.randint(0, 1)

    if num == 0:
        count_0 += 1
    else:
        count_1 += 1

    i += 1
print(f'正面的次数为{count_0:,}')
print(f'正面的次数为{count_1:,}')