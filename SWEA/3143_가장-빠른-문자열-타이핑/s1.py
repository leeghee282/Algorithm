# 3143_가장-빠른-문자열-타이핑 풀이
# 2022-06-09

import sys
sys.stdin = open('input.txt')


def my_len(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 전체 문자열, 부분 문자열 초기화
    t_str, p_str = input().split()

    # 문자열 인덱스 idx 초기화
    idx = 0
    # 각 문자열의 길이 계산
    m, n = my_len(t_str), my_len(p_str)
    # 타이핑 횟수 cnt 초기화
    cnt = 0

    # 문자열의 인덱스가 전체 문자열의 길이보다 길면 반복 중지
    while idx < m:

        # 타이핑 시, 부분 문자열을 이용할 수 있을때, 인덱스를 부분 문자열의 길이만큼 더해주고,
        # 타이핑 횟수는 1 더해주기
        if t_str[idx:idx+n] == p_str:
            idx += n
            cnt += 1
            continue

        # 부분 문자열을 이용할 수 없을 때, 인덱스와 타이핑 횟수 1 더해주기
        idx += 1
        cnt += 1

    # 결과 출력
    print('#{} {}' .format(tc, cnt))





