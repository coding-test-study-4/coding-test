N, M = map(int, input().split())
string_set = set()
count = 0

for i in range(N):
    string_set.add(input())

for i in range(M):
    string = input()
    if string in string_set:
        count += 1

print(count)
