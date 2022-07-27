count = int(input('输入范围：\n'))
i = 1
while i <= count:
    x = 2
    while x < i:
        if i % x == 0:
            break # break 不会走else
        x += 1
    else:
        print(f'{i}是一个素数')
    i += 1