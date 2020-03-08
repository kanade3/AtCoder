n = int(input())

to = [[] for _ in range(n)]
seen = [-1] * (n - 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append([b, i])

ans = [-1] * (n - 1)

print(to)


def d(index, color):
    cnt = 1
    for (t, j) in to[index]:
        if cnt == color:
            cnt += 1
        ans[j] = cnt
        d(t, cnt)
        cnt += 1


d(0, 0)
print(max(ans))
for i in ans:
    print(i)
