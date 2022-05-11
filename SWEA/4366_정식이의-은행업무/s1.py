# 4366_정식이의-은행업무
# 2022-05-11

import sys
sys.stdin = open('input.txt')

two = [0, 1]
three = [0, 1, 2]

T = int(input())

for tc in range(1, T+1):
    num_2 = list(map(int, input()))
    num_3 = list(map(int, input()))
    tmp_3 = []
    for n in num_3:
        tmp_3.append(n)
    ans_2, ans_3 = 0, 0
    ans = 0

    for i in range(len(num_2)):
        for j in range(len(num_3)):
            if num_2[i] == 1:
                num_2[i] = 0
                ans_2 = 0
                for m in range(len(num_2)):
                    ans_2 = ans_2 * 2 + num_2[m]
                for k in three:
                    if num_3[j] == k:
                        continue
                    num_3[j] = k
                    ans_3 = 0
                    for m in range(len(num_3)):
                        ans_3 = ans_3 * 3 + num_3[m]
                    if ans_2 == ans_3:
                        ans = ans_2
                        break
                    print(num_2, num_3)
                    num_3[j] = tmp_3[j]
                num_2[i] = 1

            else:
                num_2[i] = 1
                ans_2 = 0
                for m in range(len(num_2)):
                    ans_2 = ans_2 * 2 + num_2[m]
                for k in three:
                    if num_3[j] == k:
                        continue
                    num_3[j] = k
                    ans_3 = 0
                    for m in range(len(num_3)):
                        ans_3 = ans_3 * 3 + num_3[m]
                    if ans_2 == ans_3:
                        ans = ans_2
                        break
                    print(num_2, num_3)
                    num_3[j] = tmp_3[j]
                num_2[i] = 0
        if ans != 0:
            break

    print('#{} {}' .format(tc, ans))
