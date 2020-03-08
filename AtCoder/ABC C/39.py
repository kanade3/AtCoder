s = input()
sub = []
label = ['Fa', 'Mi', 'Re', 'Re', 'Do', 'Do', 'Si', 'La', 'La', 'So', 'So', 'Fa']
for i in range(14):
    sub.append(s[i:i + 6])
    if sub[i] == 'WBWBWB':
        print(label[i])
        exit(0)
