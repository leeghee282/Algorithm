# 14503_로봇-청소기
# 2022-06-06


def bfs(si, sj, sd):

    global clean
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    queue = [(si, sj, sd, 0)]
    front, rear = -1, 0
    array[si][sj] = 2
    
    while front != rear:
        front += 1
        ci, cj, cd, cnt = queue[front]
        nd = (cd + 3) % 4
        bd = (cd + 2) % 4

        ni, nj = ci + di[nd], cj + dj[nd]
        bi, bj = ci + di[bd], cj + dj[bd]

        if cnt == 4:
            if array[bi][bj] == 1:
                return
            else:
                array[bi][bj] = 2
                queue.append((bi, bj, cd, 0))
                rear += 1

        elif array[ni][nj] == 0:
            array[ni][nj] = 2
            queue.append((ni, nj, nd, 0))
            rear += 1
        
        else:
            queue.append((ci, cj, nd, cnt+1))
            rear += 1


N, M = map(int, input().split())
r, c, d = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
clean = 0

bfs(r, c, d)

for n in range(N):
    for m in range(M):
        if array[n][m] == 2:
            clean += 1

print(clean)