n = int(input())
a = list(map(int, input().split()))

d = round(sum(a) / len(a))
cost = 0
for i in a:
    cost += (i - d) ** 2

print(cost)
