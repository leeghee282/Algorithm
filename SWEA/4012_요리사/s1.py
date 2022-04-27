# 4012_요리사
# 2022-04-27

import sys
sys.stdin = open('input.txt')


def cal_taste(num_list):
    ans = 0
    for i in num_list:
        for j in num_list:
            if i != j:
                ans += arr[i][j]
    return ans


def food(idx, k):
    global min_taste

    if idx == N//2:
        A, B = [], []
        for n in range(N):
            if visit[n] == 1:
                A.append(n)
            else:
                B.append(n)
        taste1 = cal_taste(A)
        taste2 = cal_taste(B)
        if min_taste > abs(taste1 - taste2):
            min_taste = abs(taste1 - taste2)
        return

    for n in range(k, N):
        if visit[n] == 0:
            visit[n] = 1
            food(idx+1, n+1)
            visit[n] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_taste = 99999999

    food(0, 0)
    print('#{} {}' .format(tc, min_taste))