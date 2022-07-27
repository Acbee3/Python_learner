arr = [2, 2, 3, 1, 4, 4, 2, 1]

major = arr[0]
count = 0
for i in arr:
    if count == 0:
        major = i
    if i == major:
        count += 1
    else:
        count -= 1
if count > 0:
    print(major)