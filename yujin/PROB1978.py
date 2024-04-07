#소수 찾기
N = int(input())
lst = list(map(int, input().split()))
result = 0

for n in lst :
    cnt = 0
    if n>1:
        for i in range(2, n):
            if n % i == 0:
                cnt += 1
        if cnt == 0:
            result += 1

print(result)