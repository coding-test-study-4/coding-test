import sys
import math

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
res = 0

for num in nums:
    s = 0
    for d in range(2, math.ceil(num/2)+1):
        if num % d == 0:
            s += 1
            break
    if s == 0 and num != 1:
        res += 1

print(res)