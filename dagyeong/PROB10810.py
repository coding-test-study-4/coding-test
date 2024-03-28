import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(N)]

for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    arr[i-1:j] = [k] * (j - i + 1)

print(*arr)