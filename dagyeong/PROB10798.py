import sys

arr = [list(sys.stdin.readline().strip()) for _ in range(5)]

for j in range(15):
    for i in range(5):
        try:
            print(arr[i][j], end='')
        except:
            pass