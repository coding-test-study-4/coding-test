import sys
readline = sys.stdin.readline

n, m = map(int, readline().split(' '))
board = [list(readline().rstrip()) for _ in range(n)]

_min = 51

for i in range(0, n - 7):
    for j in range(0, m-7):

        bs, ws = 0, 0
        for x, row in enumerate(board[i:i+8]):
            for y, r in enumerate(row[j:j+8]):
                if (x+y+2)%2 == 0: # even
                    if r == 'B':  ws += 1
                    else:         bs += 1
                else: # odd
                    if r == 'W':  ws += 1
                    else:         bs += 1                
        res = min(bs, ws)
        if _min > res:  _min = res

print(_min)
                
                        

