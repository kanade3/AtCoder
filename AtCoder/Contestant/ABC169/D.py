n = int(input())


def prime_factorize_n(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


a_list = prime_factorize_n(n)
# print(a_list)

tmp = 1
used_list = []
for i in range(len(a_list)):
    if a_list[i] not in used_list:
        used_list.append(a_list[i])

    else:
        if tmp == 1:
            tmp = a_list[i]

        else:
            # print(i, tmp)
            if tmp % a_list[i] == 0:
                tmp *= a_list[i]
                if tmp not in used_list:
                    used_list.append(tmp)
                    tmp = 1
            else:
                tmp = a_list[i]

# print(used_list)
print(len(used_list))
