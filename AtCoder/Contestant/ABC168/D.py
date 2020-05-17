from collections import deque

n, m = map(int, input().split())

ki = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)

# print(ki)

q = deque([0])
seen = [0] * n
ans = [-1] * n
ans[0] = 0
s = 0
while len(q):
    s = q.pop()
    if seen[s] == 0:
        seen[s] = 1

    for i in ki[s]:
        if seen[i]:
            continue
        if seen[i] == 0:
            seen[i] = 1
        ans[i] = s + 1
        q.append(i)

for i in ans:
    if i == -1:
        print('No')
        exit()
print("Yes")
for i in range(1, len(ans)):
    print(ans[i])
