k = int(input())
a, b = map(int, input().split())

for i in range(1, 10001):
    if a <= i * k <= b:
        print('OK')
        exit()
print("NG")
