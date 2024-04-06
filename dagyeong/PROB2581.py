import sys
import math

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
SUM = 0
MIN = 0

for num in range(M, N+1):
    s = 0
    for d in range(2, math.ceil(num/2)+1):
        if num % d == 0:
            s += 1
            break
    if s == 0 and num != 1:
        if SUM == 0:
            MIN = num
        SUM += num

if SUM == 0:
    print(-1)
else:
    print(SUM)
    print(MIN)
