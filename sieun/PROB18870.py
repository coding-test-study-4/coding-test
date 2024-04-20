N = int(input())
numbers = list(map(int, input().split()))
numbers_set = set()
# print(numbers)

for number in numbers:
    numbers_set.add(number)
# print(numbers_set)

numbers_sorted = list(numbers_set)
numbers_sorted.sort()
# print(numbers)

numbers_dictionary = dict()
for i in range(len(numbers_sorted)):
    numbers_dictionary[numbers_sorted[i]] = i
# print(numbers_dictionary)

for number in numbers:
    print(numbers_dictionary[number], end=" ")
