n= int(input())
s = [-1]
for _ in range(n - 1):
    s.append(int(input()) - 1)
print(s)
salary = {}
for i in range(n - 1, -1, -1):
    if i not in s:
        salary[i] = 1
        print(salary)
    else:
        t = []
        for k, l in enumerate(s):
            print(k,l,i)
            if l == i:
                t.append(salary[k])
        salary[i] = 1 + min(t) + max(t)
print(salary[0])