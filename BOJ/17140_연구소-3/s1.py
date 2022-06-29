# 17140_연구소-3
# 2022-06-29


def comb(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]        
        for rest in comb(arr[i+1:], n-1):
            result.append([elem] + rest)   
    return result


def spread(arr, v_lst):
    global min_t
    tmp = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if (i, j) in v_lst:
                tmp[i][j] = 'v'
            elif arr[i][j] == 1:
                tmp[i][j] = '-'
            elif arr[i][j] == 2:
                tmp[i][j] = '*'

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    queue = []
    front, rear = -1, -1
    res = 0

    for i, j in v_lst:
        queue.append((i, j, 0))
        visit[i][j] = 1
        rear += 1

    while front != rear:
        front += 1
        ci, cj, cnt = queue[front]
        cnt += 1

        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
                if tmp[ni][nj] == 0:
                    visit[ni][nj] = 1
                    tmp[ni][nj] = cnt
                    queue.append((ni, nj, cnt))
                    rear += 1
                    if cnt > res:
                        res = cnt

                elif tmp[ni][nj] == '*':
                    visit[ni][nj] = 1
                    queue.append((ni, nj, cnt))
                    rear += 1

    for i in range(N):
        for j in range(N):
            if tmp[i][j] == 0:
                res = 9999

    return res


N, M = map(int, input().split())
LAB = [list(map(int, input().split())) for _ in range(N)]

min_t = 9999

virus = []
for i in range(N):
    for j in range(N):
        if LAB[i][j] == 2:
            virus.append((i, j))

active = comb(virus, M)

for act in active:
    visit = [[0]*N for _ in range(N)]
    t = spread(LAB, act)

    if t < min_t:
        min_t = t

if min_t == 9999:
    min_t = -1

print(min_t)