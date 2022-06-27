# 1232_사칙연산
# 2022-06-27

import sys
sys.stdin = open('input.txt')


# 후위 순회
def postorder(idx):
    if tree[idx]:
        postorder(left[idx])
        postorder(right[idx])
        # 후위 표시식 형태로 계산식 저장
        ans.append(tree[idx])


# 테스트 케이스
T = 10

for tc in range(1, T+1):
    N = int(input())

    # tree, left, right 초기화
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    # ans 초기화
    ans = []
    for _ in range(N):
        tmp = input().split()
        # 완전 이진 트리이므로, 자식이 존재한다면 왼쪽, 오른쪽 자식 모두 존재
        if len(tmp) == 4:
            left[int(tmp[0])] = int(tmp[2])
            right[int(tmp[0])] = int(tmp[3])
            tree[int(tmp[0])] = tmp[1]
        # 자식이 없는 경우
        else:
            tree[int(tmp[0])] = int(tmp[1])

    postorder(1)

    stack = []
    # 계산식 ans가 후위 표기식 형태
    for a in ans:
        # 연산자이면 계산
        if a == '+':
            ans1 = stack.pop()
            ans2 = stack.pop()
            stack.append((ans2 + ans1))
        elif a == '-':
            ans1 = stack.pop()
            ans2 = stack.pop()
            stack.append((ans2 - ans1))
        elif a == '*':
            ans1 = stack.pop()
            ans2 = stack.pop()
            stack.append((ans2 * ans1))
        elif a == '/':
            ans1 = stack.pop()
            ans2 = stack.pop()
            stack.append((ans2 / ans1))
        # 연산자가 아니면 스택에 저장
        else:
            stack.append(int(a))

    print('#{} {}' .format(tc, int(stack.pop())))