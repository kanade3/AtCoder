s = input()
w = int(input())
a = []
cnt = 0
for i in s:
    if cnt % w == 0:
        a.append(i)
    cnt += 1
print("".join(a))
