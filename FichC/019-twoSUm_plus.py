import random
length = 10000
nums = [random.randint(1, 65535) for i in range(length)]

target = int(input("输入和值：\n"))

for index in range(length - 1):
    pos = index + 1
    while pos < length - 1:
        if nums[index] + nums[pos] == target:
            print(f"数字{nums[index]}和{nums[pos]}")
        pos += 1