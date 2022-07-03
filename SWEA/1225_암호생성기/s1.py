# 1225_암호생성기
# 2022-07-03

import sys
sys.stdin = open('input.txt')

# 테스트 케이스
T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # arr의 front, rear
    front, rear = 0, 7

    n = 1

    while True:
        # n은 1 ~ 5를 순환
        if n > 5:
            n = 1

        # arr의 맨 앞자리의 수는 1 ~ 5 감소
        arr[front] -= n
        # arr 수정
        arr.append(arr[front])
        arr.pop(front)

        # arr의 끝 자리가 0보다 작을 때, 0으로 변경 후 종료
        if arr[rear] <= 0:
            arr[rear] = 0
            break

        # n 증가
        n += 1

    # 결과 출력
    print('#{} {} {} {} {} {} {} {} {}' .format(tc, *arr))
