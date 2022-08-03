matrix = [
    [1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

tMatrix = [[row[i] for row in matrix] for i in range[4]] # 列表推导式实现

# 普通方式实现
arr = []
for i in range(4):
    arr.append([])
    for row in matrix:
        arr[i].append(row[i])
        
print(arr)