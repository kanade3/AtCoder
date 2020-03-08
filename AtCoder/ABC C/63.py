n = int(input())
s = [int(input()) for _ in range(n)]
b = []
if sum(s) % 10 != 0:
    print(sum(s))
else:
    for i in s:
        if i % 10 != 0:
            b.append(i)

    print(sum(s) - min(b) if len(b) > 0 else 0)