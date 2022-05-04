# 14500_테트로미노
# 2022-05-04


def dfs(si, sj, num, cnt):
    global max_num

    if cnt == 3:
        if num > max_num:
            max_num = num
        return

    else:
        for dir in range(4):
            ni = si + di[dir]
            nj = sj + dj[dir]

            if 0 <= ni < N and 0 <= nj < M and visit1[ni][nj] == 0:
                visit1[ni][nj] = 1
                dfs(ni, nj, num + nums[ni][nj], cnt+1)
                visit1[ni][nj] = 0


def block(si, sj):
    global max_num




N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
visit1 = [[0]*M for _ in range(N)]
visit2 = [0]*4
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
max_num = 0

for i in range(N):
    for j in range(M):
        visit1[i][j] = 1
        dfs(i, j, nums[i][j], 0)
        visit1[i][j] = 0

print(max_num)