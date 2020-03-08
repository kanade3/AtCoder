s = input()
a = [0] * 26
for i in s:
    a[ord(i) - 97] += 1
amari = 0
for i in range(26):
    amari += a[i] % 2
# print(amari)
if amari == 0 or amari == 1:
    print(len(s))
else:
    print(2 * int((len(s) - amari) / (2 * amari)) + 1)
