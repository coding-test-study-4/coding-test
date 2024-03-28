import sys

N, M = map(int, sys.stdin.readline().split())

arr = [n+1 for n in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    tmp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = tmp

print(*arr)