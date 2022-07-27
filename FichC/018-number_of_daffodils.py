for i in range(100, 999):
    hundreds = i // 100
    tens = i // 10 % 10
    ones = i % 10
    if (hundreds ** 3 + tens ** 3 + ones ** 3) == i:
        print(f'{i}是水仙花数')