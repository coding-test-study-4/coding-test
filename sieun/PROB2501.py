N, K = map(int, input().split())
numbers = []

for i in range(1, N + 1):
    if N % i == 0:
        numbers.append(i)

if len(numbers) < K:
    print("0")
else:
    print(numbers[K - 1])
