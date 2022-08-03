import timeit

t_speed = timeit.repeat('t = (1, 2, 3, 4, 5)', repeat=1000)
l_speed = timeit.repeat('l = [1, 2, 3, 4, 5]', repeat=1000)

# 统计生成元组的平均速度
t_sum = 0
for each in t_speed:
    t_sum = t_sum + each
   
t_average = t_sum / len(t_speed)
   
# 统计生成列表的平均速度
l_sum = 0
for each in l_speed:
    l_sum = l_sum + each

l_average = l_sum / len(l_speed)
   
print("创建元组的平均速度是：", t_average)
print("创建列表的平均速度是：", l_average)  