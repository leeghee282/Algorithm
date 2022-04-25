# 15685_드래곤-커브
# 2022-04-25


def dragon(si, sj, dir, gen):
    # 회전방향
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    # 회전 방향을 기록하기 위한 queue
    queue = []
    queue.append(dir)

    # 주어진 시작방향으로 이동
    ni = si + di[dir]
    nj = sj + dj[dir]
    arr[ni][nj] += 1

    # 세대만큼 반복
    for _ in range(gen):
        # 끝점을 기준으로 회전
        front = len(queue)
        while True:
            # 끝점을 기준으로, 회전방향 불러오기
            front -= 1
            # 모든 회전방향을 불러왔으면, break
            if front < 0:
                break
            # 90도 회전
            n_dir = (queue[front] + 1) % 4
            ni += di[n_dir]
            nj += dj[n_dir]
            # 회전 후 좌표 표시
            arr[ni][nj] += 1
            # 회전 후, 끝점에 이어 붙이기
            # 즉, 회전방향을 queue에 추가
            queue.append(n_dir)


# 드래곤 커브 개수
N = int(input())
# 격자
arr = [[0]*101 for _ in range(101)]
# 정사각형 개수
cnt = 0

# 드래곤 커브 개수 만큼 반복
for _ in range(N):
    # 시작점, 방향, 세대
    x, y, d, g = map(int, input().split())
    # 시작점 표시
    arr[y][x] += 1
    # 드래곤 커브 함수
    dragon(y, x, d, g)

# 정사각향 개수 세기
for i in range(100):
    for j in range(100):
        if arr[i][j] >= 1 and arr[i+1][j] >= 1 and arr[i][j+1] >= 1 and arr[i+1][j+1] >= 1:
            cnt += 1

# 결과 출력
print('{}' .format(cnt))