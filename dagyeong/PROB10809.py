import sys

S = sys.stdin.readline()

for idx in range(97, 123):
    if chr(idx) in S:
        print(S.index(chr(idx)), end=' ')
    else:
        print(-1, end=' ')