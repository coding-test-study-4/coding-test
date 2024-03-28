import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i-1:j] = list(reversed(arr[i-1:j]))

print(*arr)