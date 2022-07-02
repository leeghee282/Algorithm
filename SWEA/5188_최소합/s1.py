# 5188_최소합
# 2022-07-02

import sys
sys.stdin = open('input.txt')


def hap(si, sj, s):
    global min_sum
    di = [1, 0]
    dj = [0, 1]

    if s > min_sum:
        return

    for dir in range(2):
        ni = si + di[dir]
        nj = sj + dj[dir]

        if ni == N-1 and nj == N-1:
            s += arr[N-1][N-1]
            if s < min_sum:
                min_sum = s
            return

        if 0 <= ni < N and 0 <= nj < N:
            hap(ni, nj, s + arr[ni][nj])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    min_sum = 99999999

    hap(0, 0, arr[0][0])
    print('#{} {}' .format(tc, min_sum))