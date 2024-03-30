#문자열 반복
T = int(input())

for _ in range(T):
    R,S = input().split()
    print()
    for c in S:
        print(c*int(R), end="")
    print()