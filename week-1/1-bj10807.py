import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

cnt = 0
for n in nums:
    if n == v:  cnt += 1
print(cnt)