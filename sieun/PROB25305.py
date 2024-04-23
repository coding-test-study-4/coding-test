N, k = map(int, input().split())
scores = list(map(int, input().split()))
# print(scores)
answer = 0

scores.sort()

for i in range(k):
    answer = scores[len(scores) - 1 - i]

print(answer)
