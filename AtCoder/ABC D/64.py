n = int(input())
s = input()

l_num, r_num = 0, 0
for i in s:
    if i == '(':
        l_num += 1
    elif l_num <= 0:
        r_num += 1
    else:
        l_num -= 1
print('(' * r_num + s + ')' * l_num)
