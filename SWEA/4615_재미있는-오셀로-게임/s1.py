# 4615_재미있는-오셀로-게임
# 2022-05-18

import sys
sys.stdin = open('input.txt')


def othello(si, sj, c, dir):
    global stack
    di = [1, -1, 0, 0, 1, 1, -1, -1]
    dj = [0, 0, 1, -1, 1, -1, 1, -1]

    if c == 1:
        op = 2
    else:
        op = 1

    ni = si + di[dir]
    nj = sj + dj[dir]

    if 0 <= ni < N and 0 <= nj < N:
        if arr[ni][nj] == 0:
            stack = []
            return

        if arr[ni][nj] == c:
            while stack:
                ci, cj = stack.pop()
                arr[ci][cj] = c
            return

        if arr[ni][nj] == op:
            stack.append([ni, nj])
            othello(ni, nj, c, dir)
    else:
        stack = []
        return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2], arr[N//2][N//2-1] = 1, 1
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2, 2
    stack = []

    for _ in range(M):
        j, i, color = map(int, input().split())
        arr[i-1][j-1] = color
        for d in range(8):
            othello(i-1, j-1, color, d)

    b_cnt, w_cnt = 0, 0
    for k in range(N):
        for l in range(N):
            if arr[k][l] == 1:
                b_cnt += 1
            elif arr[k][l] == 2:
                w_cnt += 1

    print('#{} {} {}' .format(tc, b_cnt, w_cnt))