N, K = map(int, input().split())
people = []
order = []

for i in range(N):
    people.append(i + 1)

# print(people)

while people:
    for i in range(K):
        if i == K - 1:
            temp = people[0]
            people.remove(temp)
            order.append(temp)

        else:
            temp = people[0]
            people.remove(temp)
            people.append(temp)

print("<" + ", ".join(map(str, order)) + ">")
