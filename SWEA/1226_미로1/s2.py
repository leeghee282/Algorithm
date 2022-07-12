# 1226_미로1 풀이
# 2022-07-12

import sys
sys.stdin = open('input.txt')


def miro(si, sj):
    global ans, front, rear

    queue = []
    front, rear = -1, -1

    queue.append([si, sj])
    rear += 1

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while front != rear:
        front += 1
        si, sj = queue[front]
        visit[si][sj] = 1

        for dir in range(4):
            ni = si + di[dir]
            nj = sj + dj[dir]

            if arr[ni][nj] == 3:
                ans = 1
                return

            if arr[ni][nj] == 0 and not visit[ni][nj]:
                queue.append([ni, nj])
                rear += 1


T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visit = [[0]*16 for _ in range(16)]
    ans = 0

    miro(1, 1)
    print('#{} {}' .format(tc, ans))