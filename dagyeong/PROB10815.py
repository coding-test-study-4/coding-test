import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
check = {k:0 for k in list(map(int, sys.stdin.readline().split()))}

for val in arr:  # 딕셔너리 속도 빠름
    if val in check:
        check[val] = 1

print(*check.values())