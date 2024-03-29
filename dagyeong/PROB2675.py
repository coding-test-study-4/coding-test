import sys

T = int(sys.stdin.readline())

for _ in range(T):
    S, R = sys.stdin.readline().split()
    for idx in range(len(R)):
        print(R[idx]*int(S), end='')
    print()