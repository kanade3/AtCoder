N = int(input())
S = input()
moji = 'b'
for i in range(1, N + 1):
    if i % 3 == 0:
        tmp = moji
        moji = 'b' + tmp + 'b'

    elif i % 3 == 1 :
        tmp = moji
        moji = 'a' + tmp + 'c'

    elif i % 3 == 2:
        tmp = moji
        moji = 'c' + tmp + 'a'
    # print(moji)
    if len(moji) >= N:
        if S == moji:
            print(i)
            exit()
        else:
            if S=='b' and N==1:
                print(0)
            else:
                print(-1)
                exit()
