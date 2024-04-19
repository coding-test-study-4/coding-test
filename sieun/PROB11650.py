N = int(input())
numbers = []

for i in range(N):
    x_and_y = list(map(int, input().split()))
    numbers.append(x_and_y)

# print(numbers)

numbers.sort(key=lambda x: (x[0], x[1]))

# print(numbers)

for i in numbers:
    print(i[0], i[1])
