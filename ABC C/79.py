op = [['+', '+', '+'], ['+', '+', '-'], ['+', '-', '+'], ['-', '+', '+'], ['+', '-', '-'], ['-', '+', '-'],
      ['-', '-', '+'], ['+', '-', '-']]

a = list(map(int, input()))

for i in range(8):
    s = a[0]
    for j in range(3):
        if op[i][j] == '+':
            s += a[j + 1]
        else:
            s -= a[j + 1]
    if s == 7:
        for k in range(3):
            print(a[k], end='')
            print(op[i][k], end='')
        print(str(a[-1])+'=7')
        exit()
