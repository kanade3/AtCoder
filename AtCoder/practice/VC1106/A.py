while (1):
    ans = 0
    n = int(input())
    if n == 0:
        exit()
    a = list(map(int, input().split()))

    for i in range(len(a)):
        if i + 3 >= len(a):
            break

        if a[i] == 2 and a[i + 1] == 0 and a[i + 2] == 2 and a[i + 3] == 0:
            ans += 1

    print(ans)
