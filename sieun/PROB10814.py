N = int(input())

users = []

for i in range(N):
    temp = list(map(str, input().split()))
    user = [int(temp[0]), temp[1], i]
    users.append(user)

# print(words)

users.sort(key=lambda x: (x[0], x[2]))

# print(words)

for i in range(N):
    print(users[i][0], users[i][1])
