number = input('输入数字：\n')
for i in range(len(number)):
    if number[i] == number[::-1][i]:
        pass
    else:
        print(f'{number}不是回文数')
        break
if i == len(number) - 1:
    print(f'{number}是回文数')