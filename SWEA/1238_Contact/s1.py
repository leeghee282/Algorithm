# 1238_Contact
# 2022-04-29

import sys
sys.stdin = open('input.txt')


def contact(start):
    queue = []
    front, rear = -1, -1

    for i in range(N//2):
        if from_list[i] == start:
            visit[from_list[i]] = 1
            queue.append([from_list[i], to_list[i]])
            rear += 1

    while front != rear:
        front += 1
        if visit[queue[front][1]] == 0:
            visit[queue[front][1]] = visit[queue[front][0]] + 1

        for j in range(N//2):
            if from_list[j] == queue[front][1]:
                if [from_list[j], to_list[j]] not in queue:
                    queue.append([from_list[j], to_list[j]])
                    rear += 1
    return


T = 10

for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    from_list, to_list = [], []
    visit = [0] * 101

    for n in range(0, N, 2):
        from_list.append(arr[n])
        to_list.append(arr[n+1])

    contact(S)
    max_idx, max_num = 0, 0

    for m in range(101):
        if visit[m] >= max_num:
            max_idx = m
            max_num = visit[m]

    print('#{} {}' .format(tc, max_idx))