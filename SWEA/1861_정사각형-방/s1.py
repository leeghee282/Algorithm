# 1861_정사각형-방
# 2022-07-04

import sys
sys.stdin = open('input.txt')


def dfs(si, sj):
    global d
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for dir in range(4):
        ni = si + di[dir]
        nj = sj + dj[dir]

        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == arr[si][sj] + 1:
                d += 1
                dfs(ni, nj)
                return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = [0] * (N**2+1)

    for i in range(N):
        for j in range(N):
            d = 1
            dfs(i, j)
            nums[arr[i][j]] = d

    max_d, min_idx = 0, 0
    for n in range(1, N**2+1):
        if nums[n] > max_d:
            max_d = nums[n]
            min_idx = n

    print('#{} {} {}' .format(tc, min_idx, max_d))