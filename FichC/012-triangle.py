n = int(input('输入层数\n'))

i = 1
while i <= n:
    j = 0
    while j < n - i:
        print(' ', end='')
        j = j + 1
    j = 0
    while j < 2 * i - 1:
        print('*', end='')
        j = j + 1
    print('')
    i += 1
    