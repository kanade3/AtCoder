m = int(input())
mm = m / 1000


def p(a):
    print(int(a))


if m / 100 < 0.1:
    print('00')
elif mm <= 5:
    print(int(mm*10) if mm >= 1 else '0{}'.format(int(m / 100)))
elif 6 <= mm <= 30:
    p(mm+50)
elif 35 <= mm <= 70:
    p((mm - 30) / 5 + 80)
elif mm > 70:
    p(89)
