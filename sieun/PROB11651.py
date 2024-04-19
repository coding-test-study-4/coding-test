N = int(input())
numbers = []

for i in range(N):
    x_and_y = list(map(int, input().split()))
    numbers.append(x_and_y)

# print(numbers)

numbers.sort(key=lambda x: (x[1], x[0]))

# print(numbers)

for i in numbers:
    print(i[0], i[1])
