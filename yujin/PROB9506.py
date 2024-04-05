#약수들의 합
while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)

    if sum(arr) == n:
        print(n, "=", end=" ")
        print(*arr, sep=" + ")  # 요소가 차례대로 출력
    else:
        print(n, "is NOT perfect.")