N = int(input())

num_str = input()
numbers = []

for i in range(N):
    numbers.append(int(num_str[i]))

print(sum(numbers))