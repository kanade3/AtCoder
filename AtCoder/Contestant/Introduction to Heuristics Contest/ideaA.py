import numpy as np

n = int(input())
a = list(map(int, input().split()))

ans = [0] * n
isheld = [0] * 26
for i in range(n):

    if i % 5 == 0:
        for z in range(26):
            if isheld[z] == 0:
                isheld[z] = 1
                ans[i] = z + 1
                break

    else:
        b = np.array(list(map(int, input().split())))
        ans[i] = int(np.argmax(b))
        isheld[int(np.argmax(b))] = 1

for i in ans:
    print(i+1)

# print(set(ans))
# print(isheld)