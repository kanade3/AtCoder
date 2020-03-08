a = [int(input()) for i in range(5)]
k = int(input())
flag = False
for i in range(5):
    for j in range(5):
        if abs(a[i] - a[j]) > k:
            flag = True
print("Yay!" if flag == False else ":(")
