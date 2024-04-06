m = int(input())
n = int(input())

min_number = 10000
sum_number = 0

for i in range(m, n + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                min_number = min(i, min_number)
                sum_number += i

            break

if sum_number == 0:
    print("-1")
else:
    print(sum_number)
    print(min_number)
