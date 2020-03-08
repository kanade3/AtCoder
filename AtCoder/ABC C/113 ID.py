n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

    # 順序を扱うため、（元の順に出力する）番目を記録する必要がある。そのリストを作成する。
    # a[i]にアペンドすることで要素数を増やすことができる
    a[i].append(int(i))

a.sort(key=lambda x: x[1])
a.sort(key=lambda x: x[0])
print(a)
count = 0
start = a[0][0]
for i in range(m):
    #  一番上の県番号を入れる。その県番号と一致しなければ、次の県番号に移動する
    if a[i][0] != start:
        start = a[i][0]
        count = 1
    else:
        count += 1
    a[i].append(count)
print(a)
a.sort(key=lambda x: x[2])

for i in range(m):
    print('%06d' % a[i][0], end='')
    print('%06d' % a[i][3])

# mohan
'''
N,M=map(int,input().split())

city=[]
for i in range(M):
  city.append(list(map(int,input().split())))
  city[i].append(int(i))
city.sort(key=lambda x:x[1])
city.sort(key=lambda x:x[0])

start=city[0][0]
count=0
for i in range(M):
  if city[i][0]!=start:
    start=city[i][0]
    count=1
  else:
    count=count+1
  city[i].append(count)
  
city.sort(key=lambda x:x[2])

for i in range(M):
  print('%06d' % city[i][0],end='')
  print('%06d' % city[i][3])
#print(city)

'''
