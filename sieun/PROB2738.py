N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    temp_A = list(map(int, input().split()))
    A.append(temp_A)

for i in range(N):
    temp_B = list(map(int, input().split()))
    B.append(temp_B)

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for i in range(N):
    for j in range(M):
        print(A[i][j], end=" ")
    print()


