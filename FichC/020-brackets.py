string = input("请输入要检测的字符串：\n")

stack = []

for index, value in enumerate(string):
    if string[0] == '}' or string[0] == ')' or string[0] == ']':
        print("不合法")
        break
    if value == '{' or value == '(' or value == '[':
        stack.append(value)
    if value == '}' or value == ')' or value == ']':
        if value == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                print("不合法")
                break
        if value == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                print("不合法")
                break
        if value == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                print("不合法")
                break
if index == len(string) - 1:
    print("合法")