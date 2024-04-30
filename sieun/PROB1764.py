N, M = map(int, input().split())
names = set()
get_answer = set()
answer = []

for i in range(N):
    name = input()
    names.add(name)

for i in range(M):
    name = input()
    if names.__contains__(name):
        get_answer.add(name)

for name in get_answer:
    answer.append(name)

answer.sort()

print(len(answer))

for name in answer:
    print(name)

