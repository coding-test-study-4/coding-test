import sys
readline = sys.stdin.readline

primes = []
for n in range(int(readline()), int(readline())+1):
    if n == 1:  continue
    
    for i in range(2, n):
        if n % i == 0: break
    else:   primes.append(n)
if primes:  print(sum(primes)); print(primes[0])
else:       print(-1)
