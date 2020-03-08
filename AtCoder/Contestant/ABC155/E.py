import math

n = input()
memo = []
for i in range(len(n)):
    if i == 0:
        a = n[0]
    else:
        print('n:' + n[i])
        b = a + str(int(n[i]) + 1)
        print('計算前' + b)
        d = int(b) * 10 ** (len(n) - len(b))
        print(int(b) * 10 ** (len(n) - len(b)))
        sub = int(n) - d
        cnt = 0
        print(sub)
        s = str(sub)
        for j in range(len(s)):
            cnt += int(j)
        memo.append(cnt)

        # 計算
        b = a + str(int(n[i]))
        a = b
        print('計算後' + a)
        #
        # print(m)
        # memo.append(m)
        # tmp = m
print(memo)
