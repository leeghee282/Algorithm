# 4831_전기버스 풀이
# 2022-05-16

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(T):
    # 이동할 수 있는 정류장 수 K, 종점인 N번 정류장, 충전기가 설치된 M개의 정류장
    K, N, M = map(int, input().split())
    # 충전기가 설치된 정류장
    stop_list = list(map(int, input().split()))

    # 버스 위치 pos, 충전 횟수 cnt 초기화
    cnt, pos = 0, 0

    # 종점에 도달하지 못하는 경우, 반복
    while (pos + K) < N:
        # 이동가능한 최대거리의 충전기가 설치된 정류장 찾기
        for go in range(K, 0, -1):
            # 이동범위 밖에 정류장이 있을 경우를 찾기 위한 변수 초기화
            e = 0
            if (pos + go) in stop_list:
                # 이동가능한 최대거리의 정류장을 찾아 현재 위치로 저장
                pos += go
                # 충전 횟수 저장
                cnt += 1
                # 이동 범위 내의 정류장이 있을 때 더해주기
                e += 1
                break

        # 이동 범위 내의 정류장이 없을 때, 결과 계산
        if e == 0:
            cnt = 0
            break

    # 결과 출력
    print('#{} {}' .format(tc+1, cnt))
