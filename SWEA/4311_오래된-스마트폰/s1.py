# 4311_오래된-스마트폰
# 2022-06-02

import sys
sys.stdin = open('input.txt')


def input_number(ans, cnt):
    global nums
    if cnt > M:
        return

    if ans < 0 or ans > 999:
        return

    if not (ans in nums):
        nums.append((ans, cnt))

    for n in available_number:
        input_number(ans*10 + n, cnt+1)


def cal(ans, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return

    if cnt > M:
        return

    if ans < 0 or ans > 999:
        return

    if ans == W:
        cnt += 1
        if cnt < min_cnt:
            min_cnt = cnt
        return

    for o in operator:
        for k in nums:
            if k[0] != 0:
                if ans < W:
                    if o == 1:
                        cal(ans + k[0], cnt + k[1] + 1)
                    elif o == 3:
                        if k[0] != 1:
                            if ans < 500:
                                cal(ans * k[0], cnt + k[1] + 1)
                else:
                    if o == 2:
                        cal(ans - k[0], cnt + k[1] + 1)
                    elif o == 4:
                        if k[0] != 1:
                            cal(ans // k[0], cnt + k[1] + 1)


T = int(input())

for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    available_number = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    W = int(input())
    nums = []
    visit = [0] * 1000

    min_cnt = 9999

    if W in available_number:
        min_cnt = 1

    for m in available_number:
        if m != 0:
            input_number(m, 1)

    for n in nums:
        if W == n[0]:
            if n[1] < min_cnt:
                min_cnt = n[1]
        cal(n[0], n[1])

    if min_cnt == 9999:
        min_cnt = -1

    print(f'#{tc} {min_cnt}')