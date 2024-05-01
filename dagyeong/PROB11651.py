import sys

N = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for idx in range(len(arr)):
    arr[idx][0], arr[idx][1] = arr[idx][1], arr[idx][0]
arr.sort()

for val1, val2 in arr:
    print(val2, val1)