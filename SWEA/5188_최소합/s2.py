# 5188_최소합
# 2022-07-02

import sys
sys.stdin = open('input.txt', 'r')


def find_path(i, j, num):
    global min_num

    if num > min_num:
        return

    if i < 0 or i >= N or j < 0 or j >= N:
        return

    if i == N-1 and j == N-1:
        num += arr[i][j]
        if num < min_num:
            min_num = num
        return
    else:
        find_path(i+1, j, num + arr[i][j])
        find_path(i, j+1, num + arr[i][j])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 99999999
    find_path(0, 0, 0)
    print('#{} {}'.format(t, min_num))