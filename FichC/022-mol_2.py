nums = [1, 2, 1, 1, 2, 3, 4, 1, 2, 2]

major_1 = major_2 = nums[0]
count_1 = count_2 = 0

for each in nums:
    if major_1 == each:
        count_1 += 1
        continue
    if count_1 == 0:
        major_1 = each
        count_1 += 1
        continue
    
    if major_2 == each:
        count_2 += 1
        continue
    if count_2 == 0:
        major_2 = each
        count_2 += 1
        continue
    
    count_1 -= 1
    count_2 -= 1
    
if nums.count(major_1) > len(nums) / 3:
    print(major_1)
if nums.count(major_2) > len(nums) / 3:
    print(major_2)