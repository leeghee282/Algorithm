# 1231_중위순회 풀이
# 2022-06-05

import sys
sys.stdin = open('input.txt')


# 중위순회 함수
def inorder(idx):
    # 인덱스가 N보다 커지면 return
    if idx > N:
        return
    if (2*idx) <= N:
        inorder(2*idx)
    ans.append(node[idx])
    if (2*idx+1) <= N:
        inorder(2*idx+1)


T = 10

for tc in range(1, T+1):
    N = int(input())
    node = [0] * (N + 1)
    ans = []

    for _ in range(N):
        arr = list(input().split())
        # 완전 이진 트리 형식이므로, 노드번호를 인덱스로 하며 값을 저장
        node[int(arr[0])] = arr[1]

    # 순회 함수 사용
    inorder(1)

    # 결과 출력
    print('#{} '.format(tc), end='')
    for i in range(N):
        if i == N-1:
            print('{}'.format(ans[i]))
        else:
            print('{}' .format(ans[i]), end='')

