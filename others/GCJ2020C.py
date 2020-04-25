t = int(input())
ans_show = []
for i in range(t):
    n = int(input())
    task = []
    ans = [] * n
    for j in range(n):
        a, b = map(int, input().split())
        task.append([a, b, j])
    sorted_task = sorted(task, key=lambda x: x[0])

    # print(sorted_task)
    # print()

    ng = 0
    task_comp_time_c = 0
    task_comp_time_j = 0
    for k in range(n):
        # print(task_comp_time_c, task_comp_time_j, task[k])
        if task_comp_time_c <= sorted_task[k][0]:
            task_comp_time_c = sorted_task[k][1]
            task[sorted_task[k][2]] = 'C'

        elif task_comp_time_j <= sorted_task[k][0]:
            task_comp_time_j = sorted_task[k][1]
            task[sorted_task[k][2]] = 'J'

        else:
            ng = 1
            break
    if not ng:
        ans_show.append("".join(task))
    else:
        ans_show.append("IMPOSSIBLE")

for i in range(t):
    print("Case #{}:".format(i + 1), end=' ')
    print(ans_show[i])
