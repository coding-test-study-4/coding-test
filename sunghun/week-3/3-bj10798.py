import sys
readline = sys.stdin.readline

board = [readline().rstrip() for _ in range(5)]
for i in range(15):
    for w in board:
        if i+1 <= len(w):    print(w[i],end='')