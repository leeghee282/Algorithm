# 1954_달팽이-숫자-활용 풀이
# 2022-05-12

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

# 우하좌상 이동
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    # 입력 받은 N*N arr 생성
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 현재의 좌표, 회전방향 초기화
    ci, cj = 0, 0
    cnt = 0

    for n in range(1, N*N+1):
        # 좌표가 지정한 방향대로 이동, n이 1부터 순차대로 대입
        arr[ci][cj] = n
        ci += di[cnt]
        cj += dj[cnt]

        # 좌표가 표를 벗어났을 때, 이미 숫자가 대입되어 존재했을 때 회전방향 전환
        if (ci < 0) or (ci >= N) or (cj < 0) or (cj >= N) or arr[ci][cj] != 0:
            # 움직임 취소
            ci -= di[cnt]
            cj -= dj[cnt]

            # 방향 전환
            cnt = (cnt + 1) % 4

            # 방향 전환 후 다시 움직임
            ci += di[cnt]
            cj += dj[cnt]

    print('#{}' .format(tc))
    print('{}' .format(arr))



