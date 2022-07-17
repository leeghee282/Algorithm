# 5209_최소-생산-비용
# 2022-07-17

import sys
sys.stdin = open('input.txt')


def factory(idx, cost):
    global min_cost
    if cost > min_cost:
        return
    if idx == N:
        if cost < min_cost:
            min_cost = cost
        return
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            factory(idx+1, cost + arr[idx][i])
            visit[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_cost = 99999999
    factory(0, 0)

    print('#{} {}' .format(tc, min_cost))