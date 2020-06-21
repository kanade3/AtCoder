n = int(input())


def convert(num):
    if num <= 26:
        return chr(64 + num)
    elif num % 26 == 0:
        return convert(num // 26 - 1) + chr(90)
    else:
        return convert(num // 26) + chr(64 + num % 26)


print(str(convert(n)).lower())
