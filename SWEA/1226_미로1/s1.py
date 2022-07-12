# 1226_미로1 풀이
# 2022-07-12

import sys
sys.stdin = open('input.txt')


def miro(si, sj):
    global ans
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for dir in range(4):
        ni = si + di[dir]
        nj = sj + dj[dir]

        if 0 <= ni < 16 and 0 <= ni < 16 and not visit[ni][nj]:
            if arr[ni][nj] == 3:
                ans = 1
                return

            if arr[ni][nj] == 0:
                visit[ni][nj] = 1
                miro(ni, nj)


T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visit = [[0]*16 for _ in range(16)]
    ans = 0

    miro(1, 1)
    print('#{} {}' .format(tc, ans))