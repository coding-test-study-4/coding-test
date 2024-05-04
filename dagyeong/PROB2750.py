import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = []

for idx in range(len(arr)):   # 선택정렬
    MIN = min(arr[idx:N])
    change = arr.index(MIN)
    tmp = arr[idx]
    arr[idx] = MIN
    arr[change] = tmp

print(*arr, sep='\n')