import sys
readline = sys.stdin.readline

readline()

n_prime = 0
for n in map(int, readline().split(' ')):
    if n == 1:  continue
    for i in range(2, n):
        if n%i == 0:    break
    else:   n_prime += 1
print(n_prime)