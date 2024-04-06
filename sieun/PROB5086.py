answer = ""

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if a > b:
        if a % b == 0:
            answer += "multiple"
        else:
            answer += "neither"
    elif a < b:
        if b % a == 0:
            answer += "factor"
        else:
            answer += "neither"
    answer += "\n"

print(answer)
