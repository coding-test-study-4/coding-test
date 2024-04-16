N = int(input())
cnt = 0

while True:
    if N % 5 == 0:
        cnt += (N // 5)
        break

    elif N < 0:
        cnt = -1
        break

    N -= 3
    cnt += 1

print(cnt)
