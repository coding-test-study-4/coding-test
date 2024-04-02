import sys
readline = sys.stdin.readline

n = int(readline())

while n != 1:
    for i in range(2, n+1):
        if n%i == 0:
            print(i)
            n = int(n/i); break