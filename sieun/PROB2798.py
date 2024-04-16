N, M = map(int, input().split())
numbers = list(map(int, input().split()))
max_sum = 0
last_idx = len(numbers)

for i in range(last_idx):
    for j in range(i + 1, last_idx):
        for k in range(j + 1, last_idx):
            sum_numbers = numbers[i] + numbers[j] + numbers[k]
            if sum_numbers <= M:
                max_sum = max(max_sum, sum_numbers)

print(max_sum)