numbers = []

for i in range(10):
    number = int(input())

    if (number % 42) not in numbers:
        numbers.append(number % 42)

print(len(numbers))

