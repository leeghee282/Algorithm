# 17779_게러맨더링-2
# 2022-07-09

N = int(input())

Arc = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

total = 0
for r in range(1, N+1):
    for c in range(1, N+1):
        total += Arc[r][c]

min_ans = 99999999

for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if x + d1 + d2 > N:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > N:
                    continue
                
                area = [[0]*(N+1) for _ in range(N+1)]
                area[x][y] = 5
                
                for i in range(1, d1+1):
                    area[x + i][y - i] = 5
                for i in range(1, d2+1):
                    area[x + i][y + i] = 5
                for i in range(1, d2+1):
                    area[x + d1 + i][y - d1 + i] = 5
                for i in range(1, d1+1):
                    area[x + d2 + i][y + d2 - i] = 5

                people = [0] * 5

                for r in range(1, x + d1):
                    for c in range(1, y + 1):
                        if area[r][c] == 5:
                            break
                        else:
                            people[0] += Arc[r][c]

                for r in range(1, x + d2 + 1):
                    for c in range(N, y, -1):
                        if area[r][c] == 5:
                            break
                        else:
                            people[1] += Arc[r][c]

                for r in range(x + d1, N + 1):
                    for c in range(1, y - d1 + d2):
                        if area[r][c] == 5:
                            break
                        else:
                            people[2] += Arc[r][c]

                for r in range(x + d2 + 1, N + 1):
                    for c in range(N, y - d1 + d2 - 1, -1):
                        if area[r][c] == 5:
                            break
                        else:
                            people[3] += Arc[r][c]

                people[4] = total - sum(people)

                ans = max(people) - min(people)
                
                if ans < min_ans:
                    min_ans = ans

print(min_ans)