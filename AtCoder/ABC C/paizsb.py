n = int(input())
a = [(input()) for i in range(n)]
es = ['s', 'o', 'x']
boin = ['a', 'i', 'u', 'e', 'o']
for i in a:
    if i[-1] in es:
        print(i + 'es')
    elif i[-1] == 'h' and i[-2] == 's':
        print(i + 'es')
    elif i[-1] == 'h' and i[-2] == 'c':
        print(i + 'es')
    elif i[-1] == 'f':
        print(i[:-1] + 'ves')
    elif i[-1] == 'e' and i[-2] == 'f':
        print(i[:-2] + 'ves')
    elif i[-1] == 'y' and i[-2] not in boin:
        print(i[:-1] + 'ies')
    else:
        print(i + 's')
