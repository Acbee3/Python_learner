import random

matrix = []
row = int(input("请输入矩阵行数：\n"))
colmn = int(input("请输入矩阵列数：\n"))

for a in range(row):
    matrix.append([])
    for b in range(colmn):
        pass
        matrix[a].append(random.randint(0, 1024))
        
min_row = [1024] * row
max_colmn = [0] * colmn

for i in range(row):
    for j in range(colmn):
        min_row[i] = min(matrix[i][j], min_row[i])
        max_colmn[j] = max(matrix[i][j], max_colmn[j])
        
for i in range(row):
    for j in range(colmn):
        if matrix[i][j] == min_row[i] and matrix[i][j] == max_colmn[j]:
            print(matrix[i][j])