import sys
readline = sys.stdin.readline

N, K = map(int, readline().split(' '))

factors = [0]
for i in range(1, N+1):
    if N % i == 0:  factors.append(i)
    if len(factors)-1 == K: print(factors[-1]); break
else:   print(0)
