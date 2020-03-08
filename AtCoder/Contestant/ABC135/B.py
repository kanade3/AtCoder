n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

diff = 0
for i in range(len(a)):
    if a[i] != b[i]:
        diff += 1
# print(a)
# print(b)
print("YES" if diff == 0 or diff == 2 else "NO")
