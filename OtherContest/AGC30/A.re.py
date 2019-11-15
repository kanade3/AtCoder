s = input()

k = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == '<':
        k[i + 1] = max(k[i + 1], k[i] + 1)

for i in reversed(range(len(s))):
    if s[i] == '>':
        k[i] = max(k[i], k[i + 1] + 1)

# print(k)
print(sum(k))