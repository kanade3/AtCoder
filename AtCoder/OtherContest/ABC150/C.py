import itertools

n = int(input())
p = input().split()
q = input().split()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[:n]
p2 = str(p).strip("[]\'")
p3 = p2.replace("\'", "")
q2 = str(q).strip("[]\'")
q3 = q2.replace("\'", "")

cnt = 0
cnta, cntb = 0, 0
for i in itertools.permutations(b, n):
    cnt += 1
    if str(i).strip('()') == p3:
        cnta = cnt
    if str(i).strip('()') == q3:
        cntb = cnt
print(abs(cnta - cntb))
