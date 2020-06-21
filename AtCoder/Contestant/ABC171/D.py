from collections import Counter

n = int(input())

a = list(map(int, input().split()))
c = Counter(a)

# print(c)
tmpsum = sum(a)

q = int(input())

for i in range(q):
    ans = tmpsum
    before, after = map(int, input().split())

    num_of_before = c[before]
    # print(c[before])

    ans += num_of_before * (after - before)
    tmpsum = ans

    c[after] += num_of_before
    c[before] = 0
    print(ans)
