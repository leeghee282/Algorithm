# 4871_그래프-경로 풀이
# 2022-05-29

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # V, E, arr, start, end 초기화
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())

    # stack 초기화
    stack = []
    # stack에 start 추가
    stack.append(start)
    # i, ans, top 초기화
    i, ans, top = 0, 0, 0

    # 종료조건이 나올때까지 반복
    while True:
        # start에서 도착점까지 arr를 비교해가며 추가
        # stack은 경로를 표시
        for i in range(len(arr)):
            if arr[i][0] == stack[top]:
                stack.append(arr[i][1])
                top += 1
                i = 0

                # 경로의 끝이 end일 경우 반복 종료
                if stack[top] == end:
                    ans = 1
                    break

        # 경로의 끝이 end일 경우 반복 종료
        if ans == 1:
            break

        # 더이상 이동할 경로가 없을 경우, 반복 종료
        if len(stack) == 1:
            break

        # 이동한 경로의 끝이 end가 아닐 경우, 경로를 끝에서부터 제거
        # arr에서도 도착하지 못한 경로 제거
        for j in range(len(arr)):
            if stack[-1] == arr[j][1] and stack[-2] == arr[j][0]:
                arr.pop(j)
                stack.pop()
                top -= 1
                i = 0
                break

    # 결과 출력
    print('#{} {}' .format(tc, ans))