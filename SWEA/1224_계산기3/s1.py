# 1224_계산기3 풀이
# 2022-07-01

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = 10

for tc in range(1, T+1):
    # 테스트 케이스의 길이 L, 계산식 cal 초기화
    L = int(input())
    cal = input()

    # 연산자 우선순위 설정
    isp = {'*': 2, '+': 1, '(': 0}
    icp = {'*': 2, '+': 1, '(': 3}

    # stack, top, ans 초기화
    stack = []
    top = -1
    ans = ''

    # 계산식 cal에서 하나씩 검사
    for i in cal:
        # 숫자일 경우 출력
        if i.isdigit():
            ans += i
        # 연산자일 경우, stack에 요소가 없을 때 추가
        elif not stack:
            stack.append(i)
            top += 1
        # 열린 괄호인 경우, stack에 추가
        elif i == '(':
            stack.append(i)
            top += 1
        # 닫힌 괄호인 경우, stack에서 열린 괄호가 나올 때까지 pop
        elif i == ')':
            while stack[top] != '(':
                ans += stack.pop()
                top -= 1
            # stack에서 열린 괄호 제거
            stack.pop()
            top -= 1
        else:
            # 연산자의 우선순위가 stack[top]의 우선순위보다 높을 때는 stack에 추가
            if icp[i] > isp[stack[top]]:
                stack.append(i)
                top += 1
            else:
                # 연산자의 우선순위가 stack[top]의 우선순위보다 낮거나 같을때
                if icp[i] <= isp[stack[top]]:
                    # 스택에 요소가 존재하고 stack[top]의 우선순위보다 낮아질 때까지 반복
                    while stack and icp[i] <= isp[stack[top]]:
                        ans += stack.pop()
                        top -= 1
                    # 반복 종료 후, 연산자를 다시 stack에 추가
                    stack.append(i)
                    top += 1

    # stack에 남아있는 요소들을 제거
    while stack:
        ans += stack.pop()
        top -= 1

    # 계산식을 후위 표기식으로 바꾼 결과를 계산
    for a in ans:
        # 숫자인 경우, stack에 추가
        if a.isdigit():
            stack.append(a)
            top += 1
        # 연산자가 +일 경우, stack에서 두 숫자를 pop을 해서 + 계산
        elif a == '+':
            op1 = stack.pop()
            top -= 1
            op2 = stack.pop()
            top -= 1
            stack.append(int(op2) + int(op1))
            top += 1
        # 연산자가 +일 경우, stack에서 두 숫자를 pop을 해서 * 계산
        elif a == '*':
            op1 = stack.pop()
            top -= 1
            op2 = stack.pop()
            top -= 1
            stack.append(int(op2) * int(op1))
            top += 1

    # 계산 종료 후, stack에 남아있는 결과를 출력
    print('#{} {}' .format(tc, stack.pop()))
