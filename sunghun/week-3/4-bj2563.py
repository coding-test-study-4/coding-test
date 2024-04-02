import sys
readline = sys.stdin.readline

n = int(readline())
board = [[0 for j in range(100)] for i in range(100)]
area = 0
for x, y in [map(int, readline().split(' ')) for _ in range(n)]:
    for i in range(10):
        for j in range(10):
            if not board[y+i][x+j]: board[y+i][x+j] = 1; area += 1

print(area)