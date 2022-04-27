# 14501_퇴사
# 2022-04-27


def counselor(idx, cost):
    global max_cost
    if idx == N-1:
        if cost > max_cost:
            max_cost = cost
        return
    else:
        if idx + T[idx] <= N-1:
            counselor(idx+T[idx], cost+P[idx])
        else:
            counselor(idx+1, cost)
        counselor(idx+1, cost)


N = int(input())
T, P = [], []
max_cost = 0

for _ in range(N):
    Ti, Pi = map(int, input().split())
    T.append(Ti)
    P.append(Pi)

counselor(0, 0)
print(max_cost)