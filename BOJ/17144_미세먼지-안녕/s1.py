# 17144_미세먼지-안녕
# 2022-06-26


def spread(arr):
    next_arr = [[0]*C for _ in range(R)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(R):
        for j in range(C):
            cnt, tmp = 0, []
            
            for d in range(4):
                si, sj = i, j
                ni = si + di[d]
                nj = sj + dj[d]
                if arr[si][sj] > 0:
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        cnt += 1
                        tmp.append((ni, nj))

            for m, n in tmp:
                next_arr[m][n] += arr[i][j] // 5
            next_arr[i][j] += arr[i][j] - ((arr[i][j]//5) * cnt)

    return next_arr


def clean(arr):
    next_arr = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            next_arr[i][j] += arr[i][j]

    di_lst = [[0, -1, 0, 1], [0, 1, 0, -1]]
    dj_lst = [[1, 0, -1, 0], [1, 0, -1, 0]]

    for c in range(2):
        di, dj = di_lst[c], dj_lst[c]
        si, sj = cleaner[c]
        sj += 1
        next_arr[si][sj] = 0

        for d in range(4):
            while True:
                ni = si + di[d]
                nj = sj + dj[d]

                if not (0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1):
                    break
                
                if arr[ni][nj] != -1:
                    next_arr[ni][nj] = arr[si][sj]

                si, sj = ni, nj
    
    return next_arr


R, C, T = map(int, input().split())

Arr = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
left_dust_arr = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if Arr[i][j] == -1:
            cleaner.append((i, j))
        left_dust_arr[i][j] += Arr[i][j]

for _ in range(T):
    left_dust_arr = spread(left_dust_arr)
    left_dust_arr = clean(left_dust_arr)

ans = 0

for i in range(R):
    for j in range(C):
        if left_dust_arr[i][j] != -1:
            ans += left_dust_arr[i][j]

print(ans)