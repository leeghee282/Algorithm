# 15686_치킨-배달
# 2022-05-31


def comb(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]        
        for rest in comb(arr[i+1:], n-1):
            result.append([elem] + rest)   
    return result


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house_p, chicken_p = [], []

min_dis = 9999999

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house_p.append((i, j))
        elif city[i][j] == 2:
            chicken_p.append((i, j))

for c in comb(chicken_p, M):
    house_dis = [100] * len(house_p)
    for p in c:
        for d in range(len(house_p)):
            dis = abs(p[0]-house_p[d][0]) + abs(p[1]-house_p[d][1])
            if dis < house_dis[d]:
                house_dis[d] = dis
    if sum(house_dis) < min_dis:
        min_dis = sum(house_dis)

print(min_dis)