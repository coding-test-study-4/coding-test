import sys

N = [int(n) for n in sys.stdin.readline().strip()]
print(*sorted(N, reverse=True), sep='')