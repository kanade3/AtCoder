n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] -= 1

memo = [0] * n

index = 0
memo_index = 0
cnt_k = 1
while 1:
    tmp_move_to = a[index]
    if not memo[tmp_move_to]:
        memo[tmp_move_to] = 1
        index = tmp_move_to
        if cnt_k == k:
            print(tmp_move_to + 1)
            exit()
        cnt_k += 1
    else:
        break
k -= cnt_k

kaburi = tmp_move_to
circle = [kaburi]

index = kaburi
while 1:
    if kaburi == a[index]:
        break
    else:
        circle.append(a[index])
        index = a[index]
# print(circle)
print(circle[k % len(circle)] + 1)
