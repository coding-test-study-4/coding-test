N = int(input())
value = 665

while N > 0:
    value += 1
    if str(value).__contains__("666"):
        N -= 1

print(value)
