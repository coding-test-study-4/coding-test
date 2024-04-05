#소수
M = int(input())
N = int(input())

s = []
for n in range(M, N+1):
    e = 0
    if n>1:
        for i in range(2, n):
            if n % i == 0:
                e += 1
                break
        if e == 0:
            s.append(n)

if len(s)>0:
    print(sum(s))
    print(min(s))
else:
    print(-1)