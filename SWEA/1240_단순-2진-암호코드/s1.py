# 1240_단순-2진-암호코드
# 2022-07-22

import sys
sys.stdin = open('input.txt')

# 암호목록
password = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
    '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = []

    # 모든 암호가 1로 끝나므로 배열의 끝에서부터 탐색
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                si, sj = i, j
                break

    # 탐색한 결과를 바탕으로 56자리 수 저장
    nums = arr[si][sj-55:sj+1]

    # 암호 목록을 사용하여 암호코드 저장
    for k in range(0, 56, 7):
       ans.append(password[nums[k:k+7]])

    # 암호코드를 검증하여 결과 출력
    if (((ans[0] + ans[2] + ans[4] + ans[6]) * 3) + ans[1] + ans[3] + ans[5] + ans[7]) % 10 == 0:
        print('#{} {}' .format(tc, ans[0] + ans[1] + ans[2] + ans[3] + ans[4] + ans[5] + ans[6] + ans[7]))
    else:
        print('#{} 0' .format(tc))
