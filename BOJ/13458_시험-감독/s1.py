# 13458_시험-감독
# 2022-06-24


N = int(input())

A = list(map(int, input().split()))

B, C = map(int, input().split())

man = N

for i in range(len(A)):
    A[i] -= B

for i in range(len(A)):
    if A[i] > 0:
        if A[i] % C == 0:
            man += A[i] // C
        else:
            man += (A[i] // C) + 1

print(man)