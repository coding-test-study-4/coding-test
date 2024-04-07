#색종이
n = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        a = i
        for j in range(x, x+10):
            b = j
            if arr[a][b] == 0:
                arr[a][b] = 1
            else:
                pass
s = 0
for i in range(100):
    s += sum(arr[i])

print(s)