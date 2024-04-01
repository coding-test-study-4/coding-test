#그대로 출력하기
while True:
    try:
        print(input())
    except EOFError: #사용자가 입력을 멈추면
        break
    