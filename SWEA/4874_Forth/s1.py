# 4874_Forth 풀이
# 2022-06-07

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 계산기 초기화
    cal = list(input().split())

    # 스택 초기화
    stack = []
    top = -1

    # 계산식 하나하나 비교
    for c in cal:
        # 숫자일 경우, 스택에 추가
        if c.isdigit():
            stack.append(int(c))
            top += 1
        # '.'일 경우, 출력
        # stack 안에 요소가 2개 이상이면 에러
        elif c == '.':
            if len(stack) == 1:
                print('#{} {}' .format(tc, stack.pop()))
            else:
                print('#{} error'.format(tc))
            break
        else:
            # stack 안에 요소가 2개 이상일 경우, 연산기호에 따라 계산
            if len(stack) >= 2:
                op1 = stack.pop()
                op2 = stack.pop()
                top -= 2

                if c == '+':
                    stack.append(op2 + op1)
                    top += 1
                elif c == '-':
                    stack.append(op2 - op1)
                    top += 1
                elif c == '*':
                    stack.append(op2 * op1)
                    top += 1
                elif c == '/':
                    stack.append(op2 // op1)
                    top += 1
            # stack 안에 요소가 1개라서 연산할 수 없는 경우, 에러
            else:
                print('#{} error'.format(tc))
                break