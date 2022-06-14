# 16234_인구-이동
# 2022-06-14


def bfs(si, sj):
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    queue = [(si, sj)]
    front, rear = -1, 0
    visit[si][sj] = 1

    p, c = 0, 0

    while front != rear:
        front += 1
        ci, cj = queue[front]

        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and L <= abs((array[ci][cj] - array[ni][nj])) <= R:
                visit[ni][nj] = 1
                queue.append((ni, nj))
                rear += 1

    for i, j in queue:
        p += array[i][j]
        c += 1

    np = p // c
    for i, j in queue:
        array[i][j] = np


N, L, R = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
day = 0

while True:
    tmp = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            tmp[y][x] = array[y][x]
    
    visit = [[0]*N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0:
                bfs(y, x)

    if array == tmp:
        break

    day += 1

print(day)