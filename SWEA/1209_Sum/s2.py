# 1209_Sum 풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = 10

for tc in range(1, T+1):
    # 100x100 2차원 배열 arr 초기화
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 대각선의 합 초기화
    dig_sum1, dig_sum2 = 0, 0
    # 최대값 초기화
    max_sum = 0

    for i in range(100):
        # 행의 합, 열의 합 초기화
        row_sum, col_sum = 0, 0

        # 행의 합 구하기
        for j in range(100):
            row_sum += arr[i][j]
        # 행의 합을 최대값과 비교
        if row_sum > max_sum:
            max_sum = row_sum

        # 열의 합 구하기
        for j in range(100):
            col_sum += arr[j][i]
        # 열의 합을 최대값과 비교
        if col_sum > max_sum:
            max_sum = col_sum

        # 각 대각선의 합 구하기
        dig_sum1 += arr[i][i]
        dig_sum2 += arr[i][99 - i]

    # 각 대각선의 합을 최대값과 비교
    if dig_sum1 > max_sum:
        max_sum = dig_sum1
    if dig_sum2 > max_sum:
        max_sum = dig_sum2

    # 결과 출력
    print('#{} {}' .format(tc, max_sum))