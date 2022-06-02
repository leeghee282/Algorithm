# 1865_동철이의-일-분배
# 2022-06-02

import sys
sys.stdin = open('input.txt')


def work(idx, ans):
    global max_ans
    if ans <= max_ans:
        return

    if idx == N:
        if ans > max_ans:
            max_ans = ans
    else:
        for j in range(N):
            if visit[j] == 0:
                visit[j] = 1
                work(idx+1, ans*(array[idx][j]/100))
                visit[j] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    max_ans = 0

    work(0, 1)

    print('#{} {:.6f}' .format(tc, max_ans*100))