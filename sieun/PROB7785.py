n = int(input())
log = dict()

for i in range(n):
    person, status = map(str, input().split())
    log[person] = status

# print(log)

people = []

for key in log:
    if log[key] == "enter":
        people.append(key)

people.sort(reverse=True)

for name in people:
    print(name)
