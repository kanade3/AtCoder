n = int(input())
w = []
for i in range(n):
    w.append((input())[::-1])
w.sort()
for i in range(n):
    print(w[i][::-1])