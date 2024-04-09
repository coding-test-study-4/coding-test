import sys

n = int(sys.stdin.readline())

res = -1
for n_b5 in range(n//5, -1, -1):
    if (n - n_b5*5) % 3 == 0:
        res = n_b5 + (n - n_b5*5) // 3
        break
print(res)
