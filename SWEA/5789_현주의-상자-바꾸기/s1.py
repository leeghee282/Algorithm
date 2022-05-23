# 5789_현주의-상자-바꾸기
# 2022-05-23

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 개수
T = int(input())

for tc in range(T):
    # N개의 상자, Q회 작업
    N, Q = map(int, input().split())

    # box_list에 N개의 0을 원소로 가지는 list
    box_list = [0] * N

    # i = 1부터 Q회 동안 반복
    for i in range(1, Q+1):
        # i가 반복되는 동안 L, R 저장
        L, R = map(int, input().split())

        # L번 상자부터 R번 상자까지의 값을 i로 변경
        for idx in range(L-1, R):
            box_list[idx] = i

    # 결과 출력 형식
    ans = ''

    # 각 원소 사이를 ' '로 구분하되, 마지막에는 ' ' 입력하지 않음
    for box in box_list:
        ans += str(box)
        if box != box_list[N-1]:
            ans += ' '

    # 결과 출력
    print('#{} {}' .format(tc+1, ans))