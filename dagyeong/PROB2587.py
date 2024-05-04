import sys

def swap(a, b): # swap 함수
    tmp = a 
    a = b
    b = tmp
    return a, b

arr = [int(sys.stdin.readline().strip()) for _ in range(5)]
avg = int(sum(arr) / 5)

# 버블 정렬
for idx1 in range(5):
    for idx2 in range(1, 5):
        if arr[idx1] < arr[idx2-1]:
            arr[idx1], arr[idx2-1] = swap(arr[idx1], arr[idx2-1])

print(avg)
print(arr[2])