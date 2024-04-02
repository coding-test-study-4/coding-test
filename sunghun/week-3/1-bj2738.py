import sys
readline = sys.stdin.readline

N, M = map(int, readline().split(' '))

a = [list(map(int, readline().split(' '))) for _ in range(N)]
b = [list(map(int, readline().split(' '))) for _ in range(N)]

for row_a, row_b in zip(a, b):
    for el_a, el_b in zip(row_a, row_b):
        print(el_a + el_b, end=' ')
    print()

# N, M = sys