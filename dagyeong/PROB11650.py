import sys

N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for val in sorted(arr): 
    print(*val, sep=' ')