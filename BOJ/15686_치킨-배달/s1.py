# 15686_치킨-배달
# 2022-05-31


def chicken(idx, dis_lst):
    global min_dis

    if M == 1:
        for k in range(len(chicken_p)):
            ans = 0
            for g in house_p:
                ans += abs(chicken_p[k][0] - g[0]) + abs(chicken_p[k][1] - g[1])
                if ans >= min_dis:
                    break

            if ans < min_dis:
                min_dis = ans
        return

    else:
        if sum(dis_lst) >= min_dis:
            return

        if idx == M:
            if sum(dis_lst) < min_dis:
                min_dis = sum(dis_lst)
            return

        for k in range(len(chicken_v)):
            if chicken_v[k] == 0:
                chicken_v[k] = 1
                chicken(idx + 1, chicken_dis(chicken_p[k], dis_lst))
                chicken_v[k] = 0


def chicken_dis(position, disc):

    for i in range(len(house_p)):
        d = abs(position[0] - house_p[i][0]) + abs(position[1] - house_p[i][1])
        if d < disc[i]:
            disc[i] = d

    return disc


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house_p, house_dis = [], []
chicken_p, chicken_v = [], []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house_p.append((i, j))
            house_dis.append(99)
        elif city[i][j] == 2:
            chicken_p.append((i, j))
            chicken_v.append(0)

min_dis = 99999999
print(chicken_p)
chicken(0, house_dis)

print(min_dis)