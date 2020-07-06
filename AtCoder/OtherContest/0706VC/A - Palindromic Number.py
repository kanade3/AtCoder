n = int(input())
n_i = str(n)
if n % 2 == 0:
    print('No')

else:
    for i in range(len(n_i) // 2):
        if n_i[i] != n_i[len(n_i) -1 - i]:
            print('No')
            exit()
    print('Yes')
