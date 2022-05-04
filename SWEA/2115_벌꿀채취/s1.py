# 2115_벌꿀채취
# 2022-05-04

import sys
sys.stdin = open('input.txt')


def work(si, sj):
    honey = []
    for o in range(M):
        if visit[si][sj + o] != 0:
            return honey
    for p in range(M):
        visit[si][sj + p] = 1
        honey.append(arr[si][sj + p])
    return honey


def part1(idx, nums):
    global max_part1
    if idx == len(lst):
        result = 0
        if sum(nums) <= C:
            for n in nums:
                result += n ** 2
            if result > max_part1:
                max_part1 = result
        return
    else:
        part1(idx+1, nums + [lst[idx]])
        part1(idx+1, nums)


def part2(idx, nums):
    global max_part2
    if idx == len(lst):
        result = 0
        if sum(nums) <= C:
            for n in nums:
                result += n ** 2
            if result > max_part2:
                max_part2 = result
        return
    else:
        part2(idx+1, nums + [lst[idx]])
        part2(idx+1, nums)


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    final = 0

    for i in range(N):
        for j in range(N-(M-1)):
            max_part1 = 0
            visit = [[0]*N for _ in range(N)]
            lst = work(i, j)
            part1(0, [])
            for x in range(N):
                for y in range(N-(M-1)):
                    max_part2 = 0
                    lst = work(x, y)
                    part2(0, [])
                    if final < max_part1 + max_part2:
                        final = max_part1 + max_part2

    print('#{} {}' .format(tc, final))