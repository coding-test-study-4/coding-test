import sys

args = map(int, sys.stdin.readline().split(' '))
def sol(a, b, c, d, e, f):
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c and d*x + e*y == f:
                return x, y
            
x, y = sol(*args)
print(f"{x} {y}")
