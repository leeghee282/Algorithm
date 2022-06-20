# 15683_감시
# 2022-06-20

import copy


def vision(idx, arr):
    global min_cnt
    mode = [
        [],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]],
    ]

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    if idx >= len(cam_lst):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    cnt += 1

                if cnt >= min_cnt:
                    return

        if cnt < min_cnt:
            min_cnt = cnt
        
        return

    cam_ni, cam_nj, cam_num = cam_lst[idx]
    
    cam_mode = mode[cam_num]

    for dir in cam_mode:
        tmp = copy.deepcopy(arr)
        for d in dir:
            ni, nj = cam_ni, cam_nj
            while True:
                ni += di[d]
                nj += dj[d]

                if 0 <= ni < N and 0 <= nj < M and tmp[ni][nj] != 6:
                    if tmp[ni][nj] == 0:
                        tmp[ni][nj] = '#'
                else:
                    break

        vision(idx+1, tmp)


N, M = map(int, input().split())

office = [list(map(int, input().split())) for _ in range(N)]

cam_lst = []

for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cam_lst.append((i, j, office[i][j]))

min_cnt = 99999999
vision(0, office)

print(min_cnt)