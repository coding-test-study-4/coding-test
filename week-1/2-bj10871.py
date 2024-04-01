import sys

N, X = list(map(int, sys.stdin.readline().split()))
A = [str(i) for i in map(int, sys.stdin.readline().split()) if i < X]
print(' '.join(A))