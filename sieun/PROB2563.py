arr = [[0] * 100 for _ in range(100)]

result = 0

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            arr[j][k] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)
