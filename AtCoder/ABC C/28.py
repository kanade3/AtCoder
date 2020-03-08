b1 = list(map(int, input().split()))
b2 = [0]

b = b2 + b1
box = []

for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            if i < j < k:
                box.append(b[i] + b[j] + b[k])
box.sort(reverse=True)
print(box[2])
