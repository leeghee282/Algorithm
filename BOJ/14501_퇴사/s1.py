# 14501_퇴사
# 2022-04-28


def counselor(idx, cost):
    global max_cost

    if idx == N:
        if cost > max_cost:
            max_cost = cost
        return
    else:
        if idx + T[idx] <= N:
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