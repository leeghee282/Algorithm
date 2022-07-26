# 4839_이진탐색 풀이
# 2022-07-26

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # P, Pa, Pb 초기화
    P, Pa, Pb = map(int, input().split())

    # 계산 과정에 필요한 l, r, c, cnt를 a, b로 나누어 초기화
    la, lb, ra, rb = 1, 1, P, P
    ca, cb = int((la + ra) / 2), int((lb + rb) / 2)
    cnt_a, cnt_b = 1, 1

    # a와 b 모두 탐색이 끝날 경우, 탐색 종료
    while (ca != Pa) or (cb != Pb):
        # c > Pa 인 경우 r = c로 지정, c를 다시 계산
        if ca > Pa:
            ra = ca
            ca = int((la + ra) / 2)
            cnt_a += 1
        # c > Pa 인 경우 l = c로 지정, c를 다시 계산
        elif ca < Pa:
            la = ca
            ca = int((la + ra) / 2)
            cnt_a += 1

        # c > Pb 인 경우 r = c로 지정, c를 다시 계산
        if cb > Pb:
            rb = cb
            cb = int((lb + rb) / 2)
            cnt_b += 1
        # c > Pb 인 경우 l = c로 지정, c를 다시 계산
        elif cb < Pb:
            lb = cb
            cb = int((lb + rb) / 2)
            cnt_b += 1

    # 게임의 승자 찾기
    if cnt_a < cnt_b:
        print('#{} A' .format(tc))
    elif cnt_a > cnt_b:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))