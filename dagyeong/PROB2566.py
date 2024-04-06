import sys

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
MAX = 0
i, j = 0, 0
for idx in range(9):
    tmp = max(arr[idx])
    if MAX < tmp:
        MAX = tmp
        i = idx
        j = arr[idx].index(tmp)

print(MAX)
print(i+1, j+1)