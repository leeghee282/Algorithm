# 20055_컨베이어-벨트-위의-로봇
# 2022-08-14

N, K = map(int, input().split())
conveyor = list(map(int, input().split()))
robot = [0] * N

turn = 1

while True:
    # 컨베이어 이동
    tmpConveyor = conveyor.pop()
    conveyor.insert(0, tmpConveyor)

    # 로봇도 이동
    robot.pop()
    robot.insert(0, 0)

    # 로봇 내리기
    robot[N-1] = 0

    robot_list = []

    # 로봇 위치 파악
    for i in range(N-1):
        if robot[i] == 1:
            robot_list.append(i)

    # 가장 먼저 올라간 로봇부터 이동
    robot_list.reverse()

    # 개별 로봇 이동
    for r in robot_list:
        if robot[r+1] == 0:
            if conveyor[r+1] > 0:
                conveyor[r+1] -= 1
                if r+1 < N-1:
                    robot[r], robot[r+1] = 0, 1
                else:
                    robot[r] = 0 #로봇내리기

    # 로봇 올리기
    if robot[0] == 0:
        if conveyor[0] > 0:
            robot[0] = 1
            conveyor[0] -= 1

    # 종료 조건 체크
    end = 0
    for i in range(2*N):
        if conveyor[i] == 0:
            end += 1

    if end >= K:
        break

    turn += 1

print(turn)