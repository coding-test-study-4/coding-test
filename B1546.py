#평균
n = int(input())
score = list(map(int, input().split()))
sum = 0

m = max(score)
for i in range(n):
    sum += score[i] / m * 100

print(sum/n)