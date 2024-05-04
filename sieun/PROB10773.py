import sys

K = int(sys.stdin.readline())
stack = []
number_sum = 0

for i in range(K):
    number = int(sys.stdin.readline())

    if number == 0:
        stack.pop()

    else:
        stack.append(number)

for i in stack:
    number_sum += i

print(number_sum)
