# 5208_전기버스2
# 2022-07-08

import sys
sys.stdin = open('input.txt')


def ebus(idx, cnt):
    global min_cnt
    if cnt > min_cnt:
        return

    if idx >= arr[0]:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    for i in range(arr[idx], 0, -1):
        ebus(idx+i, cnt+1)


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    min_cnt = 9999
    ebus(1, -1)
    print('#{} {}' .format(tc, min_cnt))