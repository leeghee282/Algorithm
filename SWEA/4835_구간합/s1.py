# 4835_구간합 풀이
# 2022-06-08
import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 개수
T = int(input())

for tc in range(T):
    # 정수의 개수 N, 구간의 개수 M, 정수는 num_list에 저장
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # max_num, min_num 초기화
    max_num = 0
    min_num = 0
    for m in range(M):
        max_num += num_list[0+m]
        min_num += num_list[0+m]

    # 이웃한 M개의 합을 ans_num에 저장하고 max_num, min_num과 비교
    for i in range(1, N-M+1):
        ans_num = 0
        for m in range(M):
            ans_num += num_list[i+m]

        if ans_num > max_num:
            max_num = ans_num
        if ans_num < min_num:
            min_num = ans_num

    # 결과 출력
    print('#{} {}' .format(tc+1, max_num - min_num))