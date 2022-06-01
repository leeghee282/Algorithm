# 14502_연구소
# 2022-06-01


def comb(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]        
        for rest in comb(arr[i+1:], n-1):
            result.append([elem] + rest)   
    return result


def bfs(v_lst):
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    queue = []
    front, rear = -1, -1

    for i, j in v_lst:
        queue.append((i, j))
        rear += 1
        
    while front != rear:
        front += 1

        ci, cj = queue[front]

        for dir in range(4):
            ni, nj = ci + di[dir], cj + dj[dir]

            if 0 <= ni < N and 0 <= nj < M and arr_wall[ni][nj] == 0:
                arr_wall[ni][nj] = 2
                queue.append((ni, nj))
                rear += 1



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


virus, emp = [], []
max_safe = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            emp.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

for c in comb(emp, 3):
    arr_wall = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr_wall[i][j] = 1
            elif arr[i][j] == 2:
                arr_wall[i][j] = 2
    safe = 0
    for y, x in c:
        arr_wall[y][x] = 1

    bfs(virus)

    for i in range(N):
        for j in range(M):
            if arr_wall[i][j] == 0:
                safe += 1

    if safe > max_safe:
        max_safe = safe

print(max_safe)