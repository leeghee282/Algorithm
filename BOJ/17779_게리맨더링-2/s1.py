# 17779_게러맨더링-2
# 2022-07-09

N = int(input())

Arc = [list(map(int, input().split())) for _ in range(N)]

standard = []

for r in range(1, N-1):
    for c in range(0, N-2):
        standard.append((r, c))

if N % 2 == 0:
    tmp = N//2
else:
    tmp = (N//2 + 1)

for x, y in standard:
    d1 = r % tmp
    d2 = N-2 - c

    for d1 in range(1, d1+1):
        for d2 in range(1, d2+1):
            area = [[0]*N for _ in range(N)]
            nr, nc = x, y

            for _ in range(d1):
                nr -= 1
                nc += 1
                area[nr][nc] = 5
            for _ in range(d2):
                nr += 1
                nc += 1
                area[nr][nc] = 5
            for _ in range(d1):
                nr += 1
                nc -= 1
                area[nr][nc] = 5
            for _ in range(d2):
                nr -= 1
                nc -= 1
                area[nr][nc] = 5

            for r in range(N):
                for c in range(N):
                    if 
            
            for r in range(N):
                for c in range(N):
                    if area[r][c] != 5:
                        if 0 <= r < y and 0 <= c <= x+d1:
                            area[r][c] = 1
                        elif 0 <= r <= y and x+d1 < c < N:
                            area[r][c] = 2
                        elif y <= r < N and 0 < c < x+d1:
                            area[r][c] = 3
                        elif y < r < N and x+d1 <= c < N:
                            area[r][c] = 4
