# 3190_뱀
# 2022-05-01


N = int(input())
board = [[0]*N for _ in range(N)]
stack = [(0, 0)]
ni, nj, dir, time = 0, 0, 0, 0

apple = int(input())
for _ in range(apple):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

L = int(input())
change_time, change_dir = [], []
change = 0
for _ in range(L):
    X, C = input().split()
    change_time.append(int(X))
    change_dir.append(C)

while True:
    time += 1

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    ni += di[dir % 4]
    nj += dj[dir % 4]

    if (ni, nj) in stack:
        break
    if not (0 <= ni < N and 0 <= nj < N):
        break

    stack.append((ni, nj))

    if board[ni][nj] != 1:
        stack.pop(0)
    else:
        board[ni][nj] = 0

    if time in change_time:
        for k in range(len(change_time)):
            if time == change_time[k]:
                change = k

        if change_dir[change] == 'L':
            dir += 1
        else:
            dir -= 1

print(time)