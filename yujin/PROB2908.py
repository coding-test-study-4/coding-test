#상수
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

if A>B:
    print(A)
if A<B:
    print(B)