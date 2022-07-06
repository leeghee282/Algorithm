# 5189_전자카트
# 2022-07-06

import sys
sys.stdin = open('input.txt')


def route(n, k):
    global min_cost
    if n == k:
        cost = 0

        num = [0] + p + [0]
        for m in range(N):
            cost += arr[num[m]][num[m+1]]
        if cost < min_cost:
            min_cost = cost
        return
    else:
        for j in range(k):
            if visit[j] == 0:
                visit[j] = 1
                p[n] = nums[j]
                route(n+1, k)
                visit[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = []
    for i in range(1, N):
        nums.append(i)
    p = [0] * (N-1)
    visit = [0] * (N-1)
    min_cost = 99999999
    route(0, N-1)
    print('#{} {}' .format(tc, min_cost))