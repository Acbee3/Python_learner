import random

matrix = []
row = int(input("请输入矩阵行数：\n"))
clomn = int(input("请输入矩阵列数：\n"))

for a in range(row):
    matrix.append([])
    # matrix[a] = 1 # 空列表不能通过下标去赋值，要用append
    for b in range(clomn):
        pass
        matrix[a].append(random.randint(0, 1024))
        # matrix[a][b] = random.randint(0, 1024) # 空列表不能通过下标去赋值，要用append
print(matrix)