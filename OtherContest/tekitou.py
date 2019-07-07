import sys


def main(argv):
    hp = argv[0]

    if argv[0] <= argv[1]:
        print("YES")
        print("1")
        exit(0)

    elif argv[2] >= argv[1]:
        print('NO')
        exit(0)
    else:
        print('YES')
        if hp % (argv[1] - argv[2]) == 0:
            show = int((hp - argv[1]) / (argv[1] - argv[2]) + 1)
            print(show)
        else:
            print(hp // (argv[1] - argv[2]))

            """
             while hp>0:
               cnt+=1
               hp-=argv[1]
               if hp<=0:
                 print('YES')
                 print(cnt)
                 exit(0)
               hp+=argv[2]
            """


if __name__ == '__main__':
    x = []
    a, b, c = map(int, input().split())
    x.append(a)
    x.append(b)
    x.append(c)
    main(x)
