import sys
readline = sys.stdin.readline

num_str = readline().rstrip()
num = int(num_str)

for n in range(0, num+1):
    if num == (n + sum([int(s) for s in str(n)])):
        print(n)
        break
else:   print(0)