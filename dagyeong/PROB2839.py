import sys

N = int(sys.stdin.readline().strip())
# cnt = 0

# while True:
    # if N % 5 == 0:
    #     cnt = N//5
    # elif N % 3 == 0:
    #     print(N//3)
        
    # else:
cnt = 5000
for x in range(N//5+1):
    for y in range(N//3+1):
        if (5*x) + (3*y) == N:
            cnt = min(cnt, x + y)
if cnt == 5000:
    print(-1)
else:
    print(cnt)