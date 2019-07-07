import sys


def main(argv):
    moji = []

    f = open(argv[0])
    line = f.readline()

    data = line[:-1].split(' ')
    n = int(data[0])
    k = int(data[1])

    line = f.readline()
    s = str(line)

    f.close()

    # print(n)
    # print(k)
    s = s.replace('.', '0')
    s = s.replace('S', '1')
    for i in s:
        moji.append(i)

    # print(moji)

    for i in range(k):
        change = 3
        # 両隣を返せるところを探す
        if i + 2 < n:
            if moji[i] == '1' and moji[i + 1] == '1' and moji[i + 2] == '1':
                moji[i] = '0'
                moji[i + 1] = '0'
                moji[i + 2] = '0'

    print(moji.count('0'))


if __name__ == '__main__':
    main(sys.argv[1:])
