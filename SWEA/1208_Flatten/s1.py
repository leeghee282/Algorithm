# 1208_Flatten 풀이
# 2022-06-01

import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 개수
T = 10

for tc in range(T):
    # N은 덤프 횟수, num_list에 상자의 높이 저장
    N = int(input())
    num_list = list(map(int, input().split()))

    for _ in range(N):
        # max_idx, min_idx, max_num, min_num 초기화
        max_idx, min_idx = 0, 0
        max_num, min_num = num_list[0], num_list[0]

        # 최대, 최소 높이의 박스 찾기
        for i in range(1, 100):
            if num_list[i] > max_num:
                max_idx = i
                max_num = num_list[i]
            if num_list[i] < min_num:
                min_idx = i
                min_num = num_list[i]

        # 평탄화
        num_list[max_idx] -= 1
        num_list[min_idx] += 1

    # 평탄화 완료 후, 최대, 최소 높이의 박스 찾기
    max_idx, min_idx = 0, 0
    max_num, min_num = num_list[0], num_list[0]
    for i in range(100):
        if num_list[i] > max_num:
            max_idx = i
            max_num = num_list[i]
        if num_list[i] < min_num:
            min_idx = i
            min_num = num_list[i]

    # 결과 출력
    print('#{} {}' .format(tc+1, num_list[max_idx] - num_list[min_idx]))
