import sys

N, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(1, N):
        if arr[i] < arr[j-1]:
            arr[i], arr[j-1] = arr[j-1], arr[i]

print(arr[N-k])