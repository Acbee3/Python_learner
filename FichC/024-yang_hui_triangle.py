level = int(input("输入层数：\n"))
arr = []
for i in range(level):
    arr.append([])
    for j in range(i + 1):
        if i < 2:
            arr[i].append(1)
            pass
        else:
            if 0 < j < i:
                arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
            else:
                arr[i].append(1)
                
print(arr)

# 输出杨辉三角形
for index in range(level):
    # 因为是三角形，所以i越小，前边需要填充的TAB越多
    for k in range((level - index) // 2):
        print('\t', end='')
    for j in range(index + 1):
        # 要形成“隔行错开”的效果，所以我们在偶数行加4个空格
        if index % 2 == 1:
            print("    ", end='')
        # 为何要使用TAB而非空格，大家可以将下面的end='\t'改成对应的空格数即可知晓
        print(arr[index][j], end='\t')
    print()