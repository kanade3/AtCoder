x, y, a, b, c = map(int, input().split())
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)

eat_r = p[:x]
eat_g = q[:y]
eat = eat_r + eat_g
sort_eat = sorted(eat)
for i in r:
    if sort_eat[0] < i:
        sort_eat.append(i)
sort_eat.sort(reverse=True)

print(sum(sort_eat[:x + y]))
