# 1221_GNS 풀이
# 2022-05-27

import sys
sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 테스트 케이스 번호 N, 케이스 길이 K 초기화
    N, K = input().split()
    K = int(K)

    # 문자열 str_arr 초기화
    str_arr = input().split()

    # 딕셔너리 초기화
    num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    # 딕셔너리를 활용해서 문자열을 숫자로 변환
    for i in range(K):
        str_arr[i] = num_dict[str_arr[i]]

    # 변환된 숫자열을 활용해서 오름차순 정렬
    for i in range(K):
        for j in range(K):
            if str_arr[i] < str_arr[j]:
                str_arr[i], str_arr[j] = str_arr[j], str_arr[i]

    # 딕셔너리를 활용해서 숫자열을 다시 문자열로 변환
    for key, value in num_dict.items():
        for i in range(K):
            if str_arr[i] == value:
                str_arr[i] = key

    # 결과 출력
    print('{}' .format(N))
    for i in range(K):
        if i == K-1:
            print(str_arr[i])
        else:
            print(str_arr[i], end=' ')