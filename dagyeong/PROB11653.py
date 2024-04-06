import sys
import math

N = int(sys.stdin.readline().strip())

if N == 1:
    print('')

while N != 1:
    for d in range(2, N+1):
        if N % d == 0:
            print(d)
            N = N // d
            break
