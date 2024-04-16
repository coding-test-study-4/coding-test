numbers = []
sums = 0

for i in range(5):
    number = int(input())
    numbers.append(number)
    sums += number

numbers.sort()

print(sums//5)
print(numbers[5//2])
