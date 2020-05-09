n = int(input())

ans = []
for i in range(n):

    a, b = map(int, input().split())
    b -= 1
    if a - 2 * b > 0 and (a - 2 * b) % 2 != 1:
        ans.append([2, b, a - 2 * b])

    elif a - 1 * b > 0 and (a - 1 * b) % 2 != 0:
        ans.append([1, b, a - 1 * b])
    else:
        ans.append([-1])
for i in range(n):
    if len(ans[i]) == 1:
        print("NO")
    else:
        print("YES")
        for j in range(ans[i][1]):
            print(ans[i][0], end=' ')
        print(ans[i][2])
