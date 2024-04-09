import sys
readline = sys.stdin.readline

N, M = map(int, readline().split(' '))
cards = list(map(int, readline().split(' ')))

err_min = 300000
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            err = M - (cards[i] + cards[j] + cards[k])
            if 0 <= err < err_min:   err_min = err

print(M - err_min)