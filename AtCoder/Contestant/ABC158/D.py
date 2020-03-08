from collections import deque

a = input()
q = int(input())
rflag = 0
b = []
for i in range(q):
    b.append(input())
# print(b)
# print(len(b[0]))
ans = deque(list(a))

for i in range(len(b)):
    if len(b[i]) == 1:
        rflag = (rflag ^ 1)
    else:
        c = int(b[i][2])
        # print("c="+b[i][2])

        if not rflag:

            if c == 1:
                # print("extend={}".format(b[i][4]))
                extend = b[i][4]
                ans.appendleft(extend)
            else:
                # print('ll')
                ans.append(b[i][4])
        else:
            if c == 1:
                ans.append(b[i][4])
            else:
                # print("extend={}".format(b[i][4]))
                extend = b[i][4]
                ans.appendleft(extend)
        # print(ans,rflag)

if not rflag:
    print("".join(ans))
else:
    h = "".join(ans)
    print(h[::-1])
