# 2105_디저트-카페
# 2022-05-03

import sys
sys.stdin = open('input.txt')


def dfs(si, sj, oi, oj, place, go):
    global max_place
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    if go == 4:
        return

    ni = si + di[go]
    nj = sj + dj[go]

    if oi == ni and oj == nj and go == 3:
        if len(place) > max_place:
            max_place = len(place)
        return

    if 0 <= ni < N and 0 <= nj < N and desert[arr[ni][nj]] != 1:
        desert[arr[ni][nj]] = 1
        dfs(ni, nj, oi, oj, place + [arr[ni][nj]], go+1)
        dfs(ni, nj, oi, oj, place + [arr[ni][nj]], go)
        desert[arr[ni][nj]] = 0

    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_place = 0

    for i in range(N):
        for j in range(N):
            desert = [0] * 101
            desert[arr[i][j]] = 1
            dfs(i, j, i, j, [arr[i][j]], 0)

    if max_place == 0:
        max_place = -1
    print('#{} {}' .format(tc, max_place))