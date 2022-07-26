# 4839_이진탐색 풀이
# 2022-07-26

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    l, r = 1, P
    c = int((l + r) / 2)
    cnt_a = 1

    while c != Pa:
        if c > Pa:
            r = c
            c = int((l + r) / 2)
            cnt_a += 1
        elif c < Pa:
            l = c
            c = int((l + r) / 2)
            cnt_a += 1

    l, r = 1, P
    c = int((l + r) / 2)
    cnt_b = 1

    while c != Pb:
        if c > Pb:
            r = c
            c = int((l + r) / 2)
            cnt_b += 1
        elif c < Pb:
            l = c
            c = int((l + r) / 2)
            cnt_b += 1

    if cnt_a < cnt_b:
        print('#{} A' .format(tc))
    elif cnt_a > cnt_b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))