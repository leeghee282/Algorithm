# 1210_ladder 풀이
# 2022-05-25

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = 10

# 진행 방향
di = [1, 0, 0] # 하
dj = [0, 1, -1] # 우좌

for tc in range(1, T+1):
    # 사다리 초기화
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for start in range(100):
        # 시작점이 존재할 경우, ci, cj, cnt 초기화
        if ladder[0][start] == 1:
            ci = 0
            cj = start
            cnt = 0

            # 도착점에 도착할 때까지 반복
            while ladder[ci][cj] != 2:
                # 설정된 진행 방향에 따라 진행
                ci += di[cnt]
                cj += dj[cnt]

                # 오른쪽으로 갈 수 있을 경우, 진행 방향을 오른쪽으로 설정
                if cj < 99:
                    if cnt == 0 and ladder[ci][cj + 1] != 0:
                        cnt += 1
                        continue

                # 오른쪽으로 가다가 사다리의 끝에 도달할 경우, 진행방향을 다시 아래로 설정
                if cnt == 1 and cj == 99:
                    cnt -= 1
                    continue

                # 오른쪽으로 가다가 더이상 오른쪽으로 갈 수 없을 경우, 진행방향을 다시 아래로 설정
                if cnt == 1 and ladder[ci][cj + 1] == 0:
                    cnt -= 1
                    continue

                # 왼쪽으로 갈 수 있을 경우, 진행 방향을 왼쪽으로 설정
                if cj > 0:
                    if cnt == 0 and ladder[ci][cj - 1] != 0:
                        cnt += 2
                        continue

                # 왼쪽으로 가다가 사다리의 끝에 도달할 경우, 진행방향을 다시 아래로 설정
                if cnt == 2 and cj == 0:
                    cnt -= 2
                    continue

                # 왼쪽으로 가다가 더이상 왼쪽으로 갈 수 없을 경우, 진행방향을 다시 아래로 설정
                if cnt == 2 and ladder[ci][cj - 1] == 0:
                    cnt -= 2
                    continue

                # 사다리의 맨 밑에 도달할 경우, 반복문을 탈출
                if ci == 99:
                    break

        # 사다리의 최종 도착점에 도달한 경우, 결과값을 출력하고 반복 종료
        if ladder[ci][cj] == 2:
            print('#{} {}'.format(N, start))
            break