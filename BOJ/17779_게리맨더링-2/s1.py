# 17779_게러맨더링-2
# 2022-07-06

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

for r, c in standard:
    d1 = r % tmp
    d2 = N-2 - c

    for d1 in range(1, d1+1):
        area = [[0]*N for _ in range(N)]
        for d2 in range(1, d2+1):
            print(d1, d2)