import sys

n = int(sys.stdin.readline())
while n != -1:
    divs = []
    # 자기자신 제외 약수 구하기
    for d in range(1, n):
        if n % d == 0:
            divs.append(d)
    if sum(divs) == n:
        print(n, '=', end=' ')
        print(*divs, sep = ' + ')
    else:
        print(n,'is NOT perfect.')
    n = int(sys.stdin.readline())