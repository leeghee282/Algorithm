# 1865_동철이의-일-분배
# 2022-06-02

import sys
sys.stdin = open('input.txt')


def perm(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in perm(arr[:i] + arr[i+1:], n-1):
            result.append([elem] + rest)

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    visit = []
    max_success = 0

    for n in range(N):
        visit.append(n)

    for p in perm(visit, N):
        success = 1
        i = 0
        for j in p:
            success *= (array[i][j]/100)
            i += 1
        if max_success < success:
            max_success = success

    print('#{} {:.6f}' .format(tc, max_success*100))