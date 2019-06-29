import fractions


def lcm(a, b):
    return (a * b) // fractions.gcd(a, b)


a, b, c, d = map(int, input().split())

# 3,4,5,6,7,8という集合がある場合、bをcで切り捨てで割り切ることで0~bまでのcで割り切れる個数を数えることができる。
# また、a-1をcで割ることで、今回だったら2までで、cで割り切れる数を求めることができる。
cntC = b // c - (a - 1) // c
cntD = b // d - (a - 1) // d

# やらかしポイント。　cとdで共通して割り切れるものは、c*dではなく、cとdの最小公倍数だから注意すること！
cntCandD = b // lcm(c, d) - (a - 1) // lcm(c, d)

# print(cntC, cntD, cntCandD)
print(b - a + 1 - cntC - cntD + cntCandD)
