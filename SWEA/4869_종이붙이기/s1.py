# 4869_종이붙이기 풀이
# 2022-06-12

import sys
sys.stdin = open('input.txt')


# 재귀함수 paper 정의
def paper(n):
    # n이 10일 경우, 종이붙이기 방법은 1
    if n == 10:
        return 1
    # n이 20일 경우, 종이붙이기 방법은 3
    if n == 20:
        return 3
    # n을 10과 20인 경우로 나누기
    else:
        return paper(n-10) + 2 * paper(n-20)


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # N 초기화
    N = int(input())

    # 결과 출력
    print('#{} {}' .format(tc, paper(N)))


