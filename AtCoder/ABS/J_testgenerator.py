import random
a=["erase","eraser","dream","dreamer"]
miss = ["r","er","s","d"]
s=""
num = 50
for i in range(num):
    rate = random.random()
    if rate >=1.00:
        j = random.randint(0, 3)
        s+=miss[j]
    else:
        j = random.randint(0, 3)
        s+=a[j]
print(s)
