import sys

A, B = sys.stdin.readline().split()
Ar = int(A[::-1])
Br = int(B[::-1])

print(max(Ar, Br))