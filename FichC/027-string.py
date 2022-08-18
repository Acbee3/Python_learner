name = 'Liu Chao'

print(name.casefold()) # 根据官方文档的提示，lower() 只能处理英文字母，而 casefold() 除了英语外，还可以处理更多其他语言的字符，比如德语……
print(name.lower())

# 如果字符串以符号字符（+，-）开头，则在符号之后进行填充。 如果指定的宽度小于原始字符串，则返回原始字符串。
print('-520'.zfill(10)) # zero fill 是-000000520 不是000000-520
print("-520".rjust(10, "0"))
print("-520".center(6, "0").zfill(10)) # 0-5200
print("I love FishC" == "I love FishC".swapcase().swapcase())