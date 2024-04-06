import sys

a, b = map(int, sys.stdin.readline().split())
while a != 0 and b != 0:
    if b % a == 0:  # 첫번째 숫자가 두번째 숫자의 약수
        print('factor')
    elif a % b == 0:    # 첫번째 숫자가 두번째 숫자의 배수
        print('multiple')
    else:   # 아무것도 아님
        print('neither')
    a, b = map(int, sys.stdin.readline().split())