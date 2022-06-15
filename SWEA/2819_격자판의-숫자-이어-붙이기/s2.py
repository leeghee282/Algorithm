# 2819_격자판의-숫자-이어-붙이기
# 2022-06-15

import sys
sys.stdin = open('input.txt')


def dfs(si, sj, num):
    # 최종 숫자가 저장될 list
    global nums
    # 방향설정
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    # 숫자가 일곱자리가 되면 세트에 추가하고 return
    if len(num) == 7:
        nums.add(num)
        return

    # 델타 탐색
    for dir in range(4):
        ni = si + di[dir]
        nj = sj + dj[dir]

        # 범위 내에 있으면 숫자를 저장해가며 dfs
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, num + str(arr[ni][nj]))


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 중복을 제거하기 위해 set 사용
    nums = set()

    # 배열의 모든 숫자에 대하여 dfs
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')

    # 결과 출력
    print('#{} {}' .format(tc, len(nums)))