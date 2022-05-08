# 2117_홈-방범-서비스
# 2022-05-08

import sys
sys.stdin = open('input.txt')


def home_sec(si, sj):
    global max_cnt

    for k in range(1, 2*N):
        cnt = 0
        cost = k * k + (k-1) * (k-1)

        for o in range(-(k+1), k):
            for p in range(-(k+1), k):
                if 0 <= si+o < N and 0 <= sj+p < N:
                    if (abs(o) + abs(p)) < k:
                        if arr[si+o][sj+p] == 1:
                            cnt += 1

        if cnt * M - cost >= 0:
            if cnt > max_cnt:
                max_cnt = cnt


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N):
        for j in range(N):
            home_sec(i, j)

    print('#{} {}' .format(tc, max_cnt))
