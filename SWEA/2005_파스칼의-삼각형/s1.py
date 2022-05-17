# 2005_파스칼의-삼각형 풀이
# 2022-05-17

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # N 초기화
    N = int(input())
    # N은 1 이상 10 이하의 정수이므로 파스칼의 삼각형 배열의 최대 개수는 55개
    arr = [0] * 55
    # 배열에서 마지막에 삽입된 숫자의 위치를 표시하기 위한 top 초기화
    top = -1

    print('#{}' .format(tc))
    # 파스칼의 삼각형 배열 출력
    for i in range(N):
        for j in range(i+1):
            # 파스칼의 삼각형의 각 줄의 첫번째, 마지막은 1
            if j == 0 or j == i:
                top += 1
                arr[top] += 1
                print('{}' .format(arr[top]), end=' ')
            # 각 줄의 위치를 표시하는 i와 top를 활용하여 파스칼의 삼각형 출력
            else:
                top += 1
                arr[top] += arr[top-i] + arr[top-i-1]
                print('{}'.format(arr[top]), end=' ')
        print()
