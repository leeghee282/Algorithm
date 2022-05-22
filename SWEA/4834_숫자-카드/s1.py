# 4834_숫자-카드 풀이
# 2022-05-22

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(T):
    # 카드 장수 N, 숫자는 num_list로 저장
    N = int(input())
    num_list = list(map(int, input()))
    num_value = []

    # 카드 숫자와 장수를 num_dict로 표현
    for key in num_list:
        cnt = 0
        for num in num_list:
            if num == key:
                cnt += 1
        num_value.append(cnt)

    num_dict = dict(zip(num_list, num_value))

    # 가장 많은 카드에 적힌 숫자와 그 카드가 몇 장인지 결정
    max_key = 0
    max_value = 0

    for key in num_dict:
        if num_dict[key] > max_value:
            max_key = key
            max_value = num_dict[max_key]

    # 카드 장수가 같은 경우가 있을 때, 그 중에서 적힌 숫자가 가장 큰 경우가 결과
    for key in num_dict:
        if num_dict[max_key] == num_dict[key]:
            if key > max_key:
                max_key = key
                max_value = num_dict[max_key]

    # 결과 출력
    print('#{} {} {}' .format(tc+1, max_key, max_value))