# 14499_주사위-굴리기
# 2022-06-16


def roll(si, sj, od):
    global ci, cj
    di = [0, 0, 0, -1, 1]
    dj = [0, 1, -1, 0, 0]

    ni = si + di[od]
    nj = sj + dj[od]

    if 0 <= ni < N and 0 <= nj < M:
        if od == 1:
            dice[1][2], dice[3][1] = dice[3][1], dice[1][2]
            tmp = [dice[1][0], dice[1][1], dice[1][2]]
            dice[1][0], dice[1][1], dice[1][2] = tmp[2], tmp[0], tmp[1]
        elif od == 2:
            dice[1][0], dice[3][1] = dice[3][1], dice[1][0]
            tmp = [dice[1][0], dice[1][1], dice[1][2]]
            dice[1][0], dice[1][1], dice[1][2] = tmp[1], tmp[2], tmp[0]
        elif od == 3:
            tmp = [dice[0][1], dice[1][1], dice[2][1], dice[3][1]]
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = tmp[3], tmp[0], tmp[1], tmp[2]
        elif od == 4:
            tmp = [dice[0][1], dice[1][1], dice[2][1], dice[3][1]]
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = tmp[1], tmp[2], tmp[3], tmp[0]
        
        if arr[ni][nj] == 0:
            arr[ni][nj] = dice[3][1]
        else:
            dice[3][1] = arr[ni][nj]
            arr[ni][nj] = 0
        
        ci, cj = ni, nj
        print(dice[1][1])
        return
    else:
        ci, cj = si, sj
        return


N, M, x, y, K =  map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dice = [[0]*3 for _ in range(4)]

order = map(int, input().split())

ci, cj = x, y

for o in order:
    result = roll(ci, cj, o)