# 4861_회문 풀이
# 2022-05-28

import sys
sys.stdin = open('input.txt')


# 회문을 찾는 함수
def pal_find(N, M, arr):
    # 행에서 회문 찾기 시작
    for i in range(N):
        for j in range(N - M + 1):
            # 회문을 검사할 문자열 초기화
            pal = ''
            # 주어진 회문의 길이만큼 문자열 저장하기
            for k in range(M):
                pal += arr[i][j + k]
            cnt = 0
            # 문자열의 시작과 끝에서 문자 하나씩 비교해가며 회문인지 검사하기
            for n in range(M//2):
                if pal[n] == pal[-(n+1)]:
                    cnt += 1
            # 저장한 문자열이 회문이면 리턴
            if cnt == M//2:
                return pal

    # 열에서 회문 찾기 시작
    for i in range(N):
        for j in range(N - M + 1):
            # 회문을 검사할 문자열 초기화
            pal = ''
            # 주어진 회문의 길이만큼 문자열 저장하기
            for k in range(M):
                pal += arr[j + k][i]
            cnt = 0
            # 문자열의 시작과 끝에서 문자 하나씩 비교해가며 회문인지 검사하기
            for n in range(M//2):
                if pal[n] == pal[-(n+1)]:
                    cnt += 1
            # 저장한 문자열이 회문이면 리턴
            if cnt == M//2:
                return pal


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # N, M, arr 초기화
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 결과 출력
    print('#{} {}' .format(tc, pal_find(N, M, arr)))
