#배수와 약수
while True:
    A, B = map(int, input().split())

    if A==0 and B==0:
        break
    elif B%A == 0:
        print("factor")
    elif A%B == 0:
        print("multiple")
    else:
        print("neither")