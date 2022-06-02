# 1209_Sum 풀이
# 2022-06-02

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    num_sum = 0
    max_sum = 0

    for i in range(100):
        num_sum = 0
        for j in range(100):
            num_sum += arr[i][j]
        if num_sum > max_sum:
            max_sum = num_sum

    for i in range(100):
        num_sum = 0
        for j in range(100):
            num_sum += arr[j][i]
        if num_sum > max_sum:
            max_sum = num_sum

    num_sum = 0
    for i in range(100):
        num_sum += arr[i][i]
        if num_sum > max_sum:
            max_sum = num_sum

    num_sum = 0
    for i in range(100):
        num_sum += arr[i][99-i]
        if num_sum > max_sum:
            max_sum = num_sum

    print('#{} {}' .format(tc, max_sum))