# 4866_괄호검사 풀이
# 2022-06-21

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # string, stack, top, ans 초기화
    string = input()
    stack = []
    top = -1
    ans = 1

    # string에서 하나씩 비교
    for s in string:
        # s가 열린 괄호일때는 stack에 추가
        if s == '(' or s == '{':
            top += 1
            stack.append(s)
        # s가 닫힌 소괄호인 경우
        if s == ')':
            # stack에 아무것도 없는 경우, 검사 중지
            if not stack:
                ans = 0
                break
            # stack[top]이 닫힌 소괄호인 경우, 스택 요소 제거
            if stack[top] == '(':
                stack.pop()
                top -= 1
            # stack[top]이 닫힌 소괄호가 아닐 경우, 검사 중지
            else:
                ans = 0
                break
        # s가 닫힌 중괄호인 경우
        if s == '}':
            # stack에 아무것도 없는 경우, 검사 중지
            if not stack:
                ans = 0
                break
            # stack[top]이 닫힌 중괄호인 경우, 스택 요소 제거
            if stack[top] == '{':
                stack.pop()
                top -= 1
            # stack에 아무것도 없는 경우, 검사 중지
            else:
                ans = 0
                break

    # 검사 종료 후, stack에 요소가 남아있을 경우 ans = 0
    if top != -1:
        ans = 0

    # 결과 출력
    print('#{} {}' .format(tc, ans))

