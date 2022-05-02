# 14888_연산자-끼워넣기
# 2022-05-02


def cals(idx, result):
    global max_num, min_num

    if idx == N-1:
        if result > max_num:
            max_num = result
        if result < min_num:
            min_num = result
        return
    else:
        for i in range(N-1):
            if visit[i] == 0:
                visit[i] = 1

                if cal[i] == '+':
                    cals(idx+1, result + nums[idx+1])
                elif cal[i] == '-':
                    cals(idx+1, result - nums[idx+1])
                elif cal[i] == '*':
                    cals(idx+1, result * nums[idx+1])
                else:
                    if result < 0:
                        cals(idx+1, -1 * (-1 * result // nums[idx+1]))
                    else:
                        cals(idx+1, result // nums[idx+1])

                visit[i] = 0


N = int(input())
nums = list(map(int, input().split()))
A, B, C, D = map(int, input().split())

cal = []
for _ in range(A):
    cal.append('+')
for _ in range(B):
    cal.append('-')
for _ in range(C):
    cal.append('*')
for _ in range(D):
    cal.append('/')

visit = [0] * (N-1)
max_num, min_num = -1000000000, 1000000000

cals(0, nums[0])
print(max_num)
print(min_num)