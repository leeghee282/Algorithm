# 14500_테트로미노
# 2022-05-30


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

            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0:
                visit[ni][nj] = 1
                dfs(ni, nj, num + nums[ni][nj], cnt+1)
                visit[ni][nj] = 0


def block(si, sj):
    global max_num

    if 0 <= si-1 < N and 0 <= si+1 < N and 0 <= sj-1 < M:
        ans = nums[si][sj]
        ans += nums[si-1][sj] + nums[si+1][sj] + nums[si][sj-1]
        if ans > max_num:
            max_num = ans

    if 0 <= si-1 < N and 0 <= si+1 < N and 0 <= sj+1 < M:
        ans = nums[si][sj]
        ans += nums[si-1][sj] + nums[si+1][sj] + nums[si][sj+1]
        if ans > max_num:
            max_num = ans
    
    if 0 <= si-1 < N and 0 <= sj-1 < M and 0 <= sj+1 < M:
        ans = nums[si][sj]
        ans += nums[si-1][sj] + nums[si][sj-1] + nums[si][sj+1]
        if ans > max_num:
            max_num = ans

    if 0 <= si+1 < N and 0 <= sj-1 < M and 0 <= sj+1 < M:
        ans = nums[si][sj]
        ans += nums[si+1][sj] + nums[si][sj-1] + nums[si][sj+1]
        if ans > max_num:
            max_num = ans


N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
max_num = 0

for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, nums[i][j], 0)
        visit[i][j] = 0

for i in range(N):
    for j in range(M):
        block(i, j)

print(max_num)