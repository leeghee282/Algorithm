# 4311_오래된-스마트폰
# 2022-06-02

import sys
sys.stdin = open('input.txt')


def input_number(ans, cnt):
    global nums

    if cnt > M:
        return

    if ans < 0 or ans > 999:
        return

    if not (ans in nums):
        nums.append((ans, cnt))
        visit[ans] = cnt

    for n in available_number:
        input_number(ans*10 + n, cnt+1)


def bfs():
    global min_cnt

    queue = []
    front, rear = -1, -1

    for n in nums:
        queue.append(n)
        rear += 1

    while front != rear:
        front += 1

        num, cnt = queue[front]

        for n in nums:
            for o in operator:
                if o == 1:
                    if 0 <= (num+n[0]) <= 999 and visit[num+n[0]] > visit[n[0]] + cnt + 1:
                        visit[num+n[0]] = visit[n[0]] + cnt + 1
                        if visit[num+n[0]] < M:
                            queue.append((num+n[0], visit[n[0]] + cnt + 1))
                            rear += 1

                elif o == 2:
                    if 0 <= (num-n[0]) <= 999 and visit[num-n[0]] > visit[n[0]] + cnt + 1:
                        visit[num-n[0]] = visit[n[0]] + cnt + 1
                        if visit[num-n[0]] < M:
                            queue.append((num-n[0], visit[n[0]] + cnt + 1))
                            rear += 1
                        
                elif o == 3:
                    if 0 <= (num*n[0]) <= 999 and visit[num*n[0]] > visit[n[0]] + cnt + 1:
                        visit[num*n[0]] = visit[n[0]] + cnt + 1
                        if visit[num*n[0]] < M:
                            queue.append((num*n[0], visit[n[0]] + cnt + 1))
                            rear += 1

                elif o == 4:
                    if n[0] != 0:
                        if 0 <= (num//n[0]) <= 999 and visit[num//n[0]] > visit[n[0]] + cnt + 1:
                            visit[num//n[0]] = visit[n[0]] + cnt + 1
                            if visit[num//n[0]] < M:
                                queue.append((num//n[0], visit[n[0]] + cnt + 1))
                                rear += 1

    if visit[W] + 1 <= M:
        if visit[W] + 1 < min_cnt:
            min_cnt = visit[W] + 1
    else:
        min_cnt = -1

    return


T = int(input())

for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    available_number = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    W = int(input())

    nums = []
    INF = int(1e9)
    visit = [INF] * 1000

    min_cnt = 9999

    for m in available_number:
        if m != 0:
            input_number(m, 1)
    
    if W == 0:
        if W in available_number:
            min_cnt = 1
    
    for n in nums:
        if W == n[0]:
            min_cnt = n[1]
    
    if min_cnt == 9999:
        bfs()

    print(f'#{tc} {min_cnt}')