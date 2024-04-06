import sys

n, k = map(int, sys.stdin.readline().split())
n_div = []

for num in range(1, n+1):
    if n % num == 0:
        n_div.append(num)

try:
    print(n_div[k-1])
except:
    print(0)