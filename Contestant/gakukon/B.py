import copy
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = copy.deepcopy(a)

w = 10 ** 9 + 7

cnta = 0
cntb = 0
for i in range(len(a)):
    for j in range(len(a) - 1, i, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]

            cnta += 1

for i in range(len(b)):
    for j in range(len(b)):
        if b[i] > b[j]:
            cntb += 1

wa = (k * (k - 1) // 2) * cntb + cnta * k
print(wa % w)
