import sys
from collections import Counter

an, bn = map(int, sys.stdin.readline().split())
A = {val:1 for val in list(map(int, sys.stdin.readline().split()))}
B = {val:3 if val in A.keys() else 2 for val in list(map(int, sys.stdin.readline().split()))}

C = A.copy()
C.update(B)

print(Counter(C.values())[1]+Counter(C.values())[2])