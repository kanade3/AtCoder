a, b, c = map(int, input().split())
pflag = mflag = False

if a + b == c:
    pflag = True
if a - b == c:
    mflag = True

if pflag and mflag:
    print('?')
elif pflag:
    print('+')
elif mflag:
    print('-')
else:
    print('!')
