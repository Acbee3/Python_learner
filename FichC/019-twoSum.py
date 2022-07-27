length = int(input("准备输入几个数？\n"))
i = 0
nums = []

while i < length:
    num = int(input("输入数字："))
    nums.append(num)
    i += 1
    
target = int(input("输入和值：\n"))

for index in range(length - 1):
    pos = index + 1
    while pos < length - 1:
        if nums[index] + nums[pos] == target:
            print(f"数字{index}和{pos}")
        pos += 1
         