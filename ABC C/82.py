import collections

n = int(input())
a = list(map(int, input().split()))
d = collections.Counter(a)

ans = 0
for key, values in d.items():
    if key < values:
        ans += values - key
    elif key > values:
        ans += values
print(ans)
