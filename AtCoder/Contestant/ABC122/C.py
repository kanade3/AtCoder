N, Q = map(int, input().split())
S = input()
a = []
an = [0] * (N + 1)
for i in range(Q):
    a.append(list(map(int, input().split())))

for i in range(N):
    an[i + 1] = an[i] + (1 if S[i:i + 2] == 'AC' else 0)
# １とか個別に値を入れるのではなく、それまでの累積値を入れることで計算を楽にする
for i in range(Q):
    print(an[a[i][1] - 1] - an[a[i][0] - 1])
# 　末尾がAでもダメなので今回は末尾を一個多く引く
