from collections import deque

N = int(input())
structure = list(map(int, input().split()))
ori_numbers = list(map(int, input().split()))
M = int(input())
new_numbers = list(map(int, input().split()))
deque = deque()

for i in range(N):
    if structure[i] == 0:
        deque.appendleft(ori_numbers[i])

for number in new_numbers:
    deque.append(number)
    print(deque.popleft(), end=" ")
