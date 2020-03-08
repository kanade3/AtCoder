a = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']
b = [1, 7, 6, 5, 4, 3, 2]
s = input()

for i in range(len(a)):
    if s==a[i]:
        print(b[i])
