# 1242_암호코드-스캔
# 2022-06-22

import sys
sys.stdin = open('input.txt')

hexadecimal = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

password = {
    '112': '0', '122': '1', '221': '2', '114': '3', '231': '4',
    '132': '5', '411': '6', '213': '7', '312': '8', '211': '9'
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    ans = []

    for i in range(N):
        binary_list = ''
        for j in range(M):
            binary = ''
            num = hexadecimal[arr[i][j]]
            while num != 0:
                binary = str(num % 2) + binary
                num = num // 2
            while len(binary) != 4:
                binary = '0' + binary
            binary_list += binary
        arr[i] = binary_list

    cnt = 0
    code, code_list = [], []
    start = 0
    n, m = 0, 4*M-1
    ans, ans_list = '', []
    length = 0
    while n < N:

        if arr[n][m] == '1':
            start = 1

        if start == 1:
            cnt += 1
            length += 1

        if start == 1 and arr[n][m] != arr[n][m-1]:
            code.append(cnt)
            cnt = 0

        if len(code) == 4:
            code_list.append(code)
            code = []

        if len(code_list) == 7 and len(code) == 3:
            code_list.append(code)
            code = []
            start, cnt = 0, 0
            ans = ''

            while length % 56 != 0:
                length += 1

            for i in range(8):
                tmp = ''
                for j in range(3):
                    tmp += str(code_list[i][j] // (length // 56))
                ans += password[tmp]

            if ans[::-1] not in ans_list:
                ans_list.append(ans[::-1])

            length = 0
            code_list = []

        if m == 1:
            n += 1
            m = 4*M
            start, cnt = 0, 0
            code = []

        m -= 1

    final = 0
    for a in ans_list:
        num = ((int(a[0]) + int(a[2]) + int(a[4]) + int(a[6])) * 3) + int(a[1]) + int(a[3]) + int(a[5]) + int(a[7])
        if num % 10 == 0:
            final += int(a[0]) + int(a[2]) + int(a[4]) + int(a[6]) + int(a[1]) + int(a[3]) + int(a[5]) + int(a[7])

    print('#{} {}' .format(tc, final))